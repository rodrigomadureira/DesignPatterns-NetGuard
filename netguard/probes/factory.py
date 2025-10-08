"""Factory para instanciar estratégias de sondagem.

Este módulo implementa o padrão Factory Method ao centralizar a criação
de objetos ``ProbeStrategy`` com base em um identificador (por exemplo,
"icmp", "tcp" ou "http").  Novas estratégias podem ser registradas
adicionando entradas ao dicionário ``_REGISTRY``.
"""

from __future__ import annotations

from typing import Dict, Type

from .base import ProbeStrategy
from .strategies.icmp import ICMPProbe
from .strategies.tcp import TCPProbe
from .strategies.http import HTTPProbe


# Registro de estratégias disponíveis.  Para adicionar uma nova estratégia,
# importe a classe correspondente e inclua-a neste dicionário.
_REGISTRY: Dict[str, Type[ProbeStrategy]] = {
    "icmp": ICMPProbe,
    "tcp": TCPProbe,
    "http": HTTPProbe,
}


def create_probe(kind: str) -> ProbeStrategy:
    """Cria uma instância de ``ProbeStrategy`` com base no tipo fornecido.

    Parameters
    ----------
    kind: str
        Identificador da sonda (por exemplo, ``"icmp"``, ``"tcp"`` ou ``"http"``).

    Returns
    -------
    ProbeStrategy
        Instância da estratégia correspondente.

    Raises
    ------
    ValueError
        Se ``kind`` não estiver registrado no dicionário ``_REGISTRY``.
    """
    key = (kind or "").lower()
    if key not in _REGISTRY:
        raise ValueError(f"Probe kind not supported: {kind}")
    cls = _REGISTRY[key]
    return cls()  # type: ignore[call-arg]