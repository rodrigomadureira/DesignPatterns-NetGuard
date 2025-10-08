"""Sonda baseada em TCP.

Esta estratégia tenta estabelecer uma conexão TCP com um host e porta
específicos.  O tempo de ida e volta (RTT) é aproximado pelo
tempo necessário para abrir e fechar a conexão.  Se a conexão
falhar, o resultado indica ``ok=False`` e inclui a exceção capturada.
"""

from __future__ import annotations

import socket
import time
from ..base import ProbeStrategy, ProbeResult


class TCPProbe(ProbeStrategy):
    """Implementação de sonda TCP."""

    def probe(self, host: str, port: int, timeout_s: float = 1.0) -> ProbeResult:
        start = time.perf_counter()
        try:
            with socket.create_connection((host, port), timeout=timeout_s):
                rtt_ms = (time.perf_counter() - start) * 1000.0
                return ProbeResult(ok=True, rtt_ms=rtt_ms)
        except Exception as exc:
            return ProbeResult(ok=False, error=str(exc))