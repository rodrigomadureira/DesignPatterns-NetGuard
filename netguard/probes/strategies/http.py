"""Sonda baseada em HTTP.

Executa uma requisição HTTP simples usando ``urllib.request`` para
verificar a disponibilidade de um endpoint.  O tempo de ida e volta (RTT)
é calculado a partir do tempo de envio da requisição até o recebimento
da resposta.  Código de status HTTP e erros são reportados no
``ProbeResult``.
"""

from __future__ import annotations

import time
from urllib import request, error
from ..base import ProbeStrategy, ProbeResult


class HTTPProbe(ProbeStrategy):
    """Implementação de sonda HTTP."""

    def probe(self, url: str, timeout_s: float = 1.0) -> ProbeResult:
        start = time.perf_counter()
        try:
            with request.urlopen(url, timeout=timeout_s) as resp:
                rtt_ms = (time.perf_counter() - start) * 1000.0
                return ProbeResult(ok=200 <= resp.status < 400, rtt_ms=rtt_ms, status=resp.status)
        except error.HTTPError as http_err:
            # HTTPError inclui um status, mas a requisição chegou ao servidor
            rtt_ms = (time.perf_counter() - start) * 1000.0
            return ProbeResult(ok=False, rtt_ms=rtt_ms, status=http_err.code, error=str(http_err))
        except Exception as exc:
            return ProbeResult(ok=False, error=str(exc))