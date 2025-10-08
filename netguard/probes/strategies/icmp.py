"""Sonda baseada em ICMP.

Esta implementação usa o comando ``ping`` disponível no sistema para
verificar a conectividade com um host.  Em ambientes onde o
comando não está disponível ou há restrições de rede, a função de
``platform_ping`` retornará ``False`` e ``None`` como RTT.
"""

from __future__ import annotations

import subprocess
import time
from typing import Tuple, Optional

from ..base import ProbeStrategy, ProbeResult


def platform_ping(host: str, count: int = 1, timeout_s: float = 1.0) -> Tuple[bool, Optional[float]]:
    """Realiza um ping no host usando o utilitário do sistema.

    Retorna uma tupla ``(ok, rtt_ms)``.  ``ok`` indica se o host respondeu.
    ``rtt_ms`` é o tempo de ida e volta em milissegundos, ou ``None`` se não
    puder ser determinado.

    Esta função tenta usar o comando ``ping`` do sistema.  Se ocorrer
    qualquer erro (por exemplo, comando ausente, falta de permissão ou
    inacessibilidade de rede), a função retorna ``(False, None)``.
    """
    try:
        # Determinar se estamos no Windows ou Unix para escolher a flag de count.
        # A flag '-c' é usada em sistemas Unix-like; '-n' no Windows.
        count_flag = "-c" if subprocess.run(["uname"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0 else "-n"
        timeout_flag = "-W" if count_flag == "-c" else "-w"
        cmd = ["ping", count_flag, str(count), timeout_flag, str(int(timeout_s)), host]
        start = time.perf_counter()
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Calcular RTT a partir da saída, caso o comando tenha sucesso.
        rtt_ms: Optional[float] = None
        if proc.returncode == 0:
            elapsed = (time.perf_counter() - start) * 1000.0
            # Tentar extrair valor da saída.
            for token in proc.stdout.split():
                if token.startswith("time="):
                    value = token.split("=")[1]
                    # Remover sufixo 'ms' se presente.
                    value = value.replace("ms", "")
                    try:
                        rtt_ms = float(value)
                    except ValueError:
                        rtt_ms = elapsed
                    break
            return True, rtt_ms if rtt_ms is not None else elapsed
        else:
            return False, None
    except Exception:
        return False, None


class ICMPProbe(ProbeStrategy):
    """Implementação de sonda ICMP.

    Usa ``platform_ping`` para enviar um único pacote ICMP e medir o tempo
    de resposta.  Em caso de falha ou exceção, retorna ``ProbeResult``
    com ``ok=False`` e a mensagem de erro no campo ``error``.
    """

    def probe(self, host: str, count: int = 1, timeout_s: float = 1.0) -> ProbeResult:
        ok: bool
        rtt: Optional[float]
        try:
            ok, rtt = platform_ping(host, count=count, timeout_s=timeout_s)
            return ProbeResult(ok=ok, rtt_ms=rtt)
        except Exception as exc:
            return ProbeResult(ok=False, error=str(exc))