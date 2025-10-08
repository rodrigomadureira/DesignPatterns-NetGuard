"""Definições base para sondas.

Este módulo define as classes básicas para as estratégias de sondagem.
`ProbeStrategy` é uma interface abstrata que todas as sondas concretas
devem implementar.  `ProbeResult` encapsula o resultado de uma sondagem,
incluindo sucesso, tempo de ida e volta (RTT), código de status HTTP e
mensagens de erro.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class ProbeResult:
    """Representa o resultado de uma sondagem.

    Attributes
    ----------
    ok: bool
        Indica se a sondagem foi bem-sucedida.
    rtt_ms: float | None
        Tempo de ida e volta em milissegundos.  Pode ser ``None`` quando
        indisponível ou se a medição falhar.
    status: int | None
        Código de status retornado (por exemplo, status HTTP).  ``None`` se
        não aplicável.
    error: str | None
        Mensagem de erro em caso de falha.
    """

    ok: bool
    rtt_ms: Optional[float] = None
    status: Optional[int] = None
    error: Optional[str] = None


class ProbeStrategy(ABC):
    """Interface para estratégias de sondagem.

    Classes concretas devem implementar o método :meth:`probe` e
    retornar um :class:`ProbeResult` descrevendo o resultado da sondagem.
    """

    @abstractmethod
    def probe(self, **kwargs) -> ProbeResult:
        """Executa a sondagem.

        Parâmetros específicos (como host, porta ou URL) devem ser passados
        via ``kwargs``.  O retorno deve ser um objeto :class:`ProbeResult`.
        """
        raise NotImplementedError