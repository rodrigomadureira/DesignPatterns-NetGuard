"""Subpackage para estratégias de sondagem e fábrica.

Este subpacote contém a definição de interface e classes de resultado
(`base.py`), as estratégias concretas de sondagem (`strategies/`) e
uma fábrica responsável por instanciar a estratégia apropriada a partir
de uma configuração ou entrada (`factory.py`).
"""

from .base import ProbeStrategy, ProbeResult
from .factory import create_probe

__all__ = [
    "ProbeStrategy",
    "ProbeResult",
    "create_probe",
]