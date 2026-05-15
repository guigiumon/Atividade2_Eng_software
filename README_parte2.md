Tarefa 2.1
1. Padrão Arquitetural Escolhido e Justificativa (Atualizado)
O padrão adotado é a Arquitetura Monolítica (Subtipo: Script de Módulo Único), integrada aos padrões de projeto Strategy e Simple Factory.

Justificativa: O monólito mantém o sistema simples e local. O Simple Factory foi adicionado para centralizar e isolar a lógica de criação das estratégias. Ele elimina condicionais complexas no fluxo principal do programa, instanciando a estratégia correta (Iniciante ou Investidor) a partir da escolha do usuário e injetando-a dinamicamente no Strategy, que realiza o cálculo.

2. Representação dos Componentes
┌────────────────────────────────────────────────────────┐
│               INTERFACE DE TERMINAL (I/O)              │
│       (Captura inputs e imprime tabelas textuais)      │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ (Parâmetros e Nível do Usuário)
┌────────────────────────────────────────────────────────┐
│             MOTOR DE CÁLCULO (CONTEXTO)                │
│       (Gerencia e aciona a estratégia ativa)           │
└──────────────────────────┬─────────────────────────────┘
                           │
            ┌──────────────┴──────────────┐
            ▼                             ▼
┌───────────────────────┐     ┌───────────────────────┐
│  STRATEGY INICIANTE   │     │ STRATEGY INVESTIDOR   │
│ (Foco em criar hábito/│     │ (Foco em otimização/  │
│  rampa mais suave)    │     │  rampa mais direta)   │
└───────────┬───────────┘     └───────────┬───────────┘
            │                             │
            └──────────────┬──────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│               ESTADO EM MEMÓRIA LOCAL                 │
│         (Listas e dicionários do Python)               │
└────────────────────────────────────────────────────────┘
3. Principais Componentes e Responsabilidades (Atualizado)
RebalanceStrategyFactory (Simple Factory): Componente responsável por receber a string ou opção digitada pelo usuário no terminal e retornar a instância correta da estratégia de cálculo, encapsulando a lógica de criação.

RebalanceContext (Strategy): Recebe a estratégia gerada pela Factory e executa o algoritmo de rampa progressiva adequado.
4. Limitação e Trade-off
Limitação (Volatilidade dos Dados): Por ser um monólito simples que roda exclusivamente na memória local (RAM), todos os dados e o progresso do planejamento são perdidos assim que o script Python encerra sua execução no terminal.

Mitigação no contexto: Como o escopo atual é puramente acadêmico para validar a lógica de engenharia de requisitos, o script iniciará com variáveis pré-carregadas (mockadas) para facilitar os testes do avaliador sem exigir digitação repetitiva.

Minha reflexão: Dado que o programa apresenta estrutura muito simples, o tipo de arquitetura escolhido é o ideal, e dado a natureza do programa de funcionar de formas diferentes dependendo do tipo de usuário que estaria utilizando o programa, o padrão de projeto strategy se mostra altamente efciente no quesito de tratar cada cliente conforme seu atual costume de investimento, e o modelo simple factory também entra de forma muito eficiente evitando a necessidade de aumentar a complexidade da criação do objeto usuário quanto a sua experiencia de investimento.

Tarefa 2.2
## 5. Demonstração e Mapeamento dos Padrões de Projeto Utilizados

### Padrão 1: Strategy
* **Categoria:** Comportamental
* **Onde foi aplicado no código:** Arquivo `main.py`. Foi aplicado na estrutura que envolve a classe abstrata `RebalanceStrategy`, suas implementações concretas (`BeginnerStrategy` e `InvestorStrategy`) e a classe de contexto `RebalanceContext`. O trecho exato de execução encontra-se dentro da função `rodar_sistema()`:
  ```python
  motor_calculo = RebalanceContext()
  motor_calculo.definir_estrategia(estrategia_escolhida)
  rampa_calculada = motor_calculo.executar_planejamento(orcamento_usuario, metas_sistema)

Diagrama de Classes Real do Projeto:
┌────────────────────────────────────────────────────────┐
│                    RebalanceContext                    │
├────────────────────────────────────────────────────────┤
│ - _strategy: RebalanceStrategy                         │
├────────────────────────────────────────────────────────┤
│ + definir_estrategia(strategy: RebalanceStrategy)      │
│ + executar_planejamento(orcamento, metas): list        │
└───────────────────────────┬──────────────────────────── Assegura Uso
                            │ (Agregação)
                            ▼
┌────────────────────────────────────────────────────────┐
│              <<Abstract>> RebalanceStrategy            │
├────────────────────────────────────────────────────────┤
│ + calcular_rampa(orcamento: Orcamento, metas: dict)    │
└───────────────────────────┬────────────────────────────
                            │
           ┌────────────────┴────────────────┐ (Herança)
           ▼                                 ▼
┌───────────────────────┐         ┌───────────────────────┐
│   BeginnerStrategy    │         │   InvestorStrategy    │
├───────────────────────┤         ├───────────────────────┤
│ + calcular_rampa(...) │         │ + calcular_rampa(...) │
└───────────────────────┘         └───────────────────────┘

### Padrão 2: Simple Factory
* **Categoria:** Criacional

* **Onde foi aplicado no código:**  Arquivo `main.py`, especificamente na classe estática `RebalanceStrategyFactory` através do método `criar_estrategia()`. Ele elimina a necessidade de condicionais complexas na função de controle principal, encapsulando a criação do objeto:

  ```python
    estrategia_escolhida = RebalanceStrategyFactory.criar_estrategia(opcao)
    Diagrama de Módulos/Instanciação Real do Projeto:

┌────────────────────────────────────────────────────────┐
│                   Interface (I/O CLI)                  │
└───────────────────────────┬────────────────────────────
                            │ (Solicita Instanciação)
                            ▼
┌────────────────────────────────────────────────────────┐
│               RebalanceStrategyFactory                 │
├────────────────────────────────────────────────────────┤
│ + criar_estrategia(nivel_usuario: str): Strategy       │
└───────────────────────────┬────────────────────────────
                            │
             ┌──────────────┴──────────────┐ (Cria e retorna)
             ▼                             ▼
┌───────────────────────┐     ┌───────────────────────┐
│   BeginnerStrategy    │     │   InvestorStrategy    │
└───────────────────────┘     └───────────────────────┘

