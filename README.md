# DesignPatterns-NetGuard
Repositório para a N1 do 2º Bimestre da matéria "Arquitetura de Software"

# 🎯 DesignPatterns-NetGuard 
**Arquitetura de Software — FESA 2025**  
Professor: *Gabriel Lara Baptista*  
Grupo: **NetGuard - Grupo 7**

---

## 🧩 Introdução

Os **Design Patterns (Padrões de Projeto)** são soluções consolidadas para problemas recorrentes de design de software.  
Eles não são código pronto, mas **modelos reutilizáveis** que orientam a construção de sistemas mais **escaláveis, coesos e de fácil manutenção**.  

> “Padrões arquiteturais ajudam. Princípios de design ajudam. Hoje todo mundo quer ser ágil, mas também é preciso ser inteligente.”  
> — *Ivar Jacobson* :contentReference[oaicite:0]{index=0}

---

## 🧠 Classificação dos Design Patterns

Os padrões são tradicionalmente divididos em três categorias principais:

| Categoria | Foco | Exemplos |
|------------|------|-----------|
| **Criacionais** | Como criar objetos | Singleton, Factory Method, Abstract Factory, Builder, Prototype |
| **Estruturais** | Como organizar e compor classes/objetos | Adapter, Facade, Composite, Decorator, Proxy, Bridge |
| **Comportamentais** | Como os objetos interagem | Strategy, Observer, Command, Template Method, State, Chain of Responsibility |

Fonte: [Refactoring.Guru – Design Patterns](https://refactoring.guru/design-patterns/classification)

---

## 💡 Padrões Escolhidos

No contexto do **NetGuard** — uma plataforma proativa de monitoramento e rastreabilidade de incidentes de rede —  
foram implementados **dois padrões** que se encaixam perfeitamente na arquitetura atual do projeto:

### ⚙️ 1. Strategy (Comportamental)
**Problema:**  
A necessidade de realizar diferentes tipos de sondagem (ICMP, TCP, HTTP) fazia o código ficar cheio de condicionais `if/elif`.

**Solução:**  
Encapsulamos cada tipo de sonda em uma *estratégia intercambiável*, todas herdando da interface `ProbeStrategy`.  
Assim, podemos alternar dinamicamente o tipo de monitoramento.

**Benefícios:**
- Baixo acoplamento entre os tipos de sonda  
- Facilidade para adicionar novos métodos (ex.: DNS, SNMP)  
- Testabilidade e extensibilidade

**Trade-offs:**
- Cria mais classes e abstrações (complexidade inicial um pouco maior)

---

### 🏭 2. Factory Method (Criacional)
**Problema:**  
Era necessário instanciar dinamicamente a estratégia correta de sondagem sem usar múltiplos `if`s.

**Solução:**  
Implementamos uma *fábrica centralizada* (`create_probe(kind)`) que cria objetos de forma polimórfica conforme o tipo solicitado.

**Benefícios:**
- Centraliza a lógica de criação  
- Facilita integração com configurações dinâmicas  
- Segue o princípio **Open/Closed (OCP)** — aberto para extensão, fechado para modificação

**Trade-offs:**
- Introduz uma indireção extra (camada de abstração de criação)

---

## 🏗️ Estrutura do Projeto

```bash
DesignPatterns-NetGuardTeam/
│
├── netguard/
│   ├── probes/
│   │   ├── base.py          # Interface e estrutura comum (ProbeStrategy, ProbeResult)
│   │   ├── factory.py       # Implementação do Factory Method
│   │   └── strategies/
│   │       ├── icmp.py      # Estratégia ICMP
│   │       ├── tcp.py       # Estratégia TCP
│   │       └── http.py      # Estratégia HTTP
│   └── __init__.py
│
├── tests/
│   └── test_probes.py       # Testes automatizados com Pytest
│
├── main_demo.py             # Script de demonstração
├── requirements.txt
└── README.md
