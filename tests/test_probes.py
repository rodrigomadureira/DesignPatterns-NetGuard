"""Testes unitários para as estratégias de sondagem.

Estes testes verificam que cada estratégia implementada retorna um
objeto :class:`ProbeResult` e que o atributo ``ok`` é um booleano.  Os
testes não presumem que o host ou porta estão disponíveis; eles
apenas garantem que a chamada não lança exceções e que o retorno
segue o contrato definido em ``ProbeStrategy``.
"""

from __future__ import annotations

import pytest

from netguard.probes.base import ProbeResult
from netguard.probes.factory import create_probe


@pytest.mark.parametrize(
    "kind,args",
    [
        ("icmp", {"host": "localhost"}),
        ("tcp", {"host": "localhost", "port": 80}),
        ("http", {"url": "http://example.com"}),
    ],
)
def test_probes_return_probe_result(kind: str, args: dict) -> None:
    """Cada probe deve retornar um objeto ProbeResult com atributo ok."""
    probe = create_probe(kind)
    result = probe.probe(**args)
    assert isinstance(result, ProbeResult)
    # ok deve ser bool
    assert isinstance(result.ok, bool)