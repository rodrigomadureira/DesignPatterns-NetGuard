"""Coleção de estratégias concretas de sondagem.

Cada módulo neste pacote implementa uma classe que herda de
``ProbeStrategy`` e executa um tipo de sondagem específico, como
ICMP, TCP ou HTTP.  Ao adicionar um novo tipo de sonda, crie um
arquivo e registre a classe correspondente em ``netguard.probes.factory``.
"""

from .icmp import ICMPProbe
from .tcp import TCPProbe
from .http import HTTPProbe

__all__ = [
    "ICMPProbe",
    "TCPProbe",
    "HTTPProbe",
]