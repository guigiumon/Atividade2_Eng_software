# Atividade2_Eng_software

1.1

# Tema: Programa de organização financeira

O sistema resolve a dificuldade de planejamento financeiro pessoal ao sugerir divisões de renda em pilares de gastos essenciais, lazer e investimentos. O diferencial estratégico é o uso de um reequilíbrio progressivo, que ajusta as porcentagens de forma gradual para evitar mudanças bruscas que causam o abandono do plano. Os usuários principais são indivíduos que buscam saúde financeira, mas falham em métodos rígidos de economia. O problema é relevante pois a falta de uma transição suave na gestão de gastos leva à frustração e ao endividamento. Ao atuar como um guia consultivo adaptável, o software transforma o planejamento em um processo sustentável, permitindo que o usuário visualize sua real capacidade de consumo enquanto constrói, passo a passo, uma base sólida de investimentos e segurança patrimonial.

1.2

# Compreensão do Problema

1. Como você descreveria o seu processo atual para decidir quanto do seu salário pode ser gasto com lazer ou hobbies sem comprometer o fechamento do mês?

2. Ao receber uma sugestão de como dividir seu dinheiro, quais fatores fariam você confiar e seguir esse planejamento em vez de ignorá-lo?

3. O que, na sua visão, é o maior impeditivo para que você consiga manter uma constância mensal nos seus investimentos hoje?

# Fluxos de Trabalho e Rotinas

4. Descreva o passo a passo de como você planeja o seu mês: você costuma fazer uma projeção de gastos antes de receber o salário ou apenas registra o que já gastou?

5. Com que frequência você gostaria de receber sugestões de ajuste no seu orçamento (ex: apenas no início do mês, semanalmente ou sempre que surgir um gasto inesperado)?

# Frustrações e Limitações (Soluções Atuais)

6. Se você já buscou dicas de finanças ou usou simuladores, por que sentiu que aquelas divisões sugeridas (como "poupe 20%") nem sempre se aplicavam à sua realidade atual?

7. Qual é a sua maior dificuldade ao tentar categorizar um gasto por conta própria? O que torna confuso decidir se algo é um "hobby", um "essencial" ou apenas um "extra"?

# Encerramento

8. Se um sistema lhe sugerisse uma divisão de renda que exigisse um corte nos seus hobbies para aumentar seus investimentos, que tipo de informação ou visualização te convenceria de que essa sugestão é benéfica a longo prazo?

**Minha reflexão: A organização financeira é algo que muitas pessoas parecem ter sob controle, mas a minoria tem um real planejamento a ser seguido o que faz com que as pessoas fiquem na falsa ilusão de controle. Sendo assim, as perguntas além de deixar claro as adaptações necessárias para o projeto ainda poderiam fazer os clientes perceberem que seu planejamento atual possa não ser tão adequando, aumentando ainda a chance de adesão ao app.** 

1.3

Histórias:

1. Sugestão de Orçamento Adaptativa
Como um usuário que tem dificuldade em poupar, quero receber uma sugestão de divisão de renda que se ajuste gradualmente aos meus gastos atuais para que eu consiga criar o hábito de investir sem sofrer um impacto financeiro brusco no primeiro mês.

Critérios de Aceitação:

-O sistema deve permitir a entrada da renda mensal e dos gastos atuais por categoria.

-O algoritmo deve calcular uma "rampa de transição", limitando o aumento da porcentagem de investimento a um teto máximo configurável (ex: 5% de mudança por mês).

-O sistema deve exibir a diferença entre a situação atual e a meta final desejada.

Prioridade: Alta.

Justificativa: Esta é a funcionalidade central e o diferencial competitivo do sistema para garantir a retenção e evitar o abandono do plano pelo usuário.

2. Categorização Simplificada de Gastos
Como um planejador iniciante, quero ser orientado sobre como classificar meus gastos entre essenciais, lazer e investimentos para que eu entenda onde meu dinheiro está sendo realmente alocado.

Critérios de Aceitação:

-O sistema deve apresentar uma lista de exemplos ou "dicas" para cada categoria no momento do preenchimento.

-O usuário deve conseguir editar os valores de cada pilar a qualquer momento.

-O sistema deve emitir um alerta caso a soma das categorias inseridas ultrapasse 100% da renda informada.

Prioridade: Alta.

Justificativa: É a base de dados do sistema; sem uma entrada de dados clara e correta, as sugestões de planejamento perdem a validade.

3. Visualização de Evolução e Metas
Como um usuário focado em resultados, quero visualizar um gráfico de projeção que mostre em quanto tempo atingirei o equilíbrio ideal de gastos para que eu me mantenha motivado a seguir as recomendações.

Critérios de Aceitação:

-Deve existir um painel visual (gráfico de linhas ou barras) mostrando a progressão mensal das porcentagens.

-O sistema deve indicar visualmente em qual etapa do "reequilíbrio" o usuário se encontra.

-O gráfico deve destacar a estimativa de crescimento do pilar de investimentos ao longo de 6 ou 12 meses.

Prioridade: Média.

Justificativa: Funciona como um reforço positivo (feedback visual), essencial para manter o engajamento do usuário no longo prazo.

4. Simulação de Impacto de Hobbies
Como uma pessoa que valoriza seu tempo livre, quero simular como um aumento nos gastos com hobbys afetaria meu tempo para atingir o equilíbrio financeiro para que eu tome decisões de lazer conscientes.

Critérios de Aceitação:

-O sistema deve permitir alterar o valor do pilar "Lazer/Hobby" em uma área de simulação (Sandbox).

-O sistema deve recalcular automaticamente o tempo necessário para o reequilíbrio com base no novo valor.

-Deve haver uma opção de "Desfazer" para retornar ao planejamento sugerido originalmente.

Prioridade: Baixa.

Justificativa: É uma funcionalidade de suporte à decisão que traz valor agregado, mas o sistema ainda funciona sem ela.

5. Ajuste de Rota por Imprevistos
Como um usuário sujeito a variações financeiras, quero informar gastos emergenciais no mês para que o sistema recalcule a rampa de transição sem que eu precise reiniciar todo o planejamento do zero.

Critérios de Aceitação:

-O usuário deve poder marcar um gasto como "Excepcional/Emergencial" para que ele não altere a média histórica de gastos essenciais.

-O sistema deve oferecer a opção de estender o prazo de reequilíbrio progressivo em um mês para compensar o imprevisto.

-O sistema deve registrar um log ou histórico dessas exceções para análise futura.

Prioridade: Média.

Justificativa: Essencial para a resiliência do sistema, pois imprevistos são a causa comum de desistência em planejamentos financeiros rígidos.

**Minha reflexão: As histórias geradas aprensentam uma interessante gama de perfis desde uma pessoa mais organizada e controlada até uma pessoa não muito acostumada a organizar seu dinheiro e/ou não possuem uma rigidez quanto a seguir um planejamento e gastar demais com lazer, o que fornece várias visões sobre diferente aspectos que o programa deve tratar para conseguir lidar com os mais diversos casos, além de dar ideias diferentes do que o simples planejado pelo projeto, podendo assim auxiliar um grupo maior de pessoas.**

1.4

Análise da História 1: Sugestão de Orçamento Adaptativa

Como um usuário que tem dificuldade em poupar, quero receber uma sugestão de divisão de renda que se ajuste gradualmente aos meus gastos atuais para que eu consiga criar o hábito de investir sem sofrer um impacto financeiro brusco.

1. Ambiguidades nos Critérios de Aceitação:

"Teto máximo configurável": Não está claro se essa configuração é feita pelo usuário final ou se é um parâmetro fixo do sistema (hardcoded). Se o usuário puder configurar um teto de 0.1%, o reequilíbrio pode levar décadas, perdendo o propósito.

"Gastos atuais por categoria": O termo "categoria" é vago. O sistema deve aceitar categorias livres ou o usuário deve obrigatoriamente mapear seus gastos para os três pilares (Essencial, Lazer, Investimento) já na entrada?

2. Conflitos Potenciais:

Pode haver conflito com a História 2 (Categorização Simplificada). Se a História 2 permitir que o usuário crie categorias personalizadas que não se encaixem nos três pilares estratégicos, o algoritmo da História 1 não saberá como processar esses dados para calcular a "rampa".

3. Informações para Elucidação:

Qual é o "estado final" ideal padrão? O sistema deve sugerir um modelo fixo (ex: 50-30-20) ou o usuário define onde quer chegar e o sistema apenas traça o caminho progressivo?


Análise da História 5: Ajuste de Rota por Imprevistos

Como um usuário sujeito a variações financeiras, quero informar gastos emergenciais no mês para que o sistema recalcule a rampa de transição sem que eu precise reiniciar todo o planejamento do zero.

1. Ambiguidades nos Critérios de Aceitação:

"Recalcular a rampa": O sistema deve recalcular apenas o mês seguinte ou diluir a perda ao longo de todo o restante do cronograma?

"Marcar gasto como emergencial": Não há limite definido para o que pode ser marcado como emergencial. O usuário poderia, hipoteticamente, marcar todos os excessos de lazer como "emergência" para burlar a métrica de desempenho do sistema.

2. Conflitos Potenciais:

Há um conflito lógico com a História 3 (Visualização de Evolução). Se o gráfico de projeção for estático, um imprevisto na História 5 tornará o gráfico da História 3 mentiroso. O sistema precisará de um requisito de "sincronização de projeção" em tempo real.

3. Informações para Elucidação:

Existe um limite de imprevistos por semestre? Se o usuário tiver emergências todos os meses, o "reequilíbrio progressivo" nunca sairá do lugar. É necessário definir com o usuário se o sistema deve emitir um alerta de "plano inviável" após sucessivos imprevistos.

**Revisão crítica no caso de ter que cortar o escopo pela metade: A história 3 do usurário focado em resultados poderia ser cortado, pois analisando seu histórico acredita-se que ele já tenha um conhecimento sobre a gestão financeira básica e o escopo do projeto seria mais para a distribuição da renda básica do cliente e para esse cliente seria mais interessante um gestor de investimentos. Os usuários 4 e 5 poderiam ser retirados dependendo de como o novo escopo do programa seja feito, no caso de cuidar apenas de usuários com renda controlada ambos poderiam ser retirados**