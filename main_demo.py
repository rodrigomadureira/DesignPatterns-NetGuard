"""Script de demonstração para sondas do NetGuard.

Este script cria diferentes sondas usando a fábrica e realiza
sondagens simples, imprimindo os resultados.  Ele pode ser
executado diretamente via ``python main_demo.py``.
"""

from __future__ import annotations

from netguard.probes.factory import create_probe


def main() -> None:
    # Demonstração de sondagem ICMP
    try:
        icmp_probe = create_probe("icmp")
        res_icmp = icmp_probe.probe(host="localhost")
        print("ICMP localhost:", res_icmp)
    except Exception as exc:
        print("Falha ao executar ICMPProbe:", exc)

    # Demonstração de sondagem TCP
    try:
        tcp_probe = create_probe("tcp")
        res_tcp = tcp_probe.probe(host="localhost", port=80)
        print("TCP localhost:80:", res_tcp)
    except Exception as exc:
        print("Falha ao executar TCPProbe:", exc)

    # Demonstração de sondagem HTTP
    try:
        http_probe = create_probe("http")
        res_http = http_probe.probe(url="http://example.com")
        print("HTTP example.com:", res_http)
    except Exception as exc:
        print("Falha ao executar HTTPProbe:", exc)


if __name__ == "__main__":
    main()