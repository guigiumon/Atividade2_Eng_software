Tarefa 2.1
O padrão adotado é a Arquitetura Monolítica (Subtipo: Script de Módulo Único), integrada internamente ao padrão de projeto Strategy.

Justificativa: Como o sistema é um script local em Python puro focado em algoritmos, que roda inteiramente na memória do terminal (CLI) e sem banco de dados, o monólito evita a complexidade desnecessária de rede ou servidores. O padrão Strategy justifica-se diretamente pelas histórias de usuário que exigem flexibilidade no cálculo (como a História 1 e 4), permitindo alternar as regras de transição conforme a maturidade financeira do usuário (Iniciante vs. Já Investidor) sem poluir o código com condicionais (if/else).

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
3. Principais Componentes e Responsabilidades
Módulo I/O (Interface): Executa as funções input() para capturar renda/gastos (História 2) e print() para renderizar a projeção futura das metas em texto (História 3).

Contexto do Motor (RebalanceContext): Atua como a ponte que recebe os dados do usuário e injeta a estratégia de cálculo correta de acordo com o nível de maturidade selecionado no terminal.

Estratégias de Cálculo (BeginnerStrategy / InvestorStrategy): Funções matemáticas puras isoladas que aplicam as regras da rampa progressiva. A estratégia de Iniciante prioriza pequenos ajustes para não sufocar o lazer de quem está começando; a de Investidor assume que o usuário já tem disciplina e aplica cortes mais eficientes no orçamento (História 1 e 4).

Gerenciador de Emergências: Função acessória que intercepta e recalcula o plano em memória temporária caso o usuário declare um gasto excepcional no ciclo (História 5).

4. Limitação e Trade-off
Limitação (Volatilidade dos Dados): Por ser um monólito simples que roda exclusivamente na memória local (RAM), todos os dados e o progresso do planejamento são perdidos assim que o script Python encerra sua execução no terminal.

Mitigação no contexto: Como o escopo atual é puramente acadêmico para validar a lógica de engenharia de requisitos, o script iniciará com variáveis pré-carregadas (mockadas) para facilitar os testes do avaliador sem exigir digitação repetitiva.

Minha reflexão: Dado que o programa apresenta estrutura muito simples, o tipo de arquitetura escolhido é o ideal, e dado a natureza do programa de funcionar de formas diferentes dependendo do tipo de usuário que estaria utilizando o programa, o padrão de projeto strategy se mostra altamente efciente no quesito de tratar cada cliente conforme seu atual costume de investimento.

