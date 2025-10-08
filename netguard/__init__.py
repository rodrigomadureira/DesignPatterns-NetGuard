"""Root package for NetGuard probes.

Este pacote fornece componentes para sondagem de disponibilidade e
desempenho de serviços de rede.  Os módulos internos implementam
estratégias de sondagem (padrão Strategy) e uma fábrica para instanciá‑las
(padrão Factory Method).
"""

from .probes.base import ProbeStrategy, ProbeResult  # Reexport for convenience

__all__ = [
    "ProbeStrategy",
    "ProbeResult",
]