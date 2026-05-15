import unittest
from main import (
    RebalanceStrategyFactory, 
    RebalanceContext, 
    BeginnerStrategy, 
    InvestorStrategy, 
    Orcamento
)

class TestConsultorFinanceiro(unittest.TestCase):

    # =====================================================================
    # CONJUNTO DE TESTES 1: REBALANCESTRATEGYFACTORY (SIMPLE FACTORY)
    # =====================================================================

    def test_factory_sucesso_iniciante(self):
        """Cenário de Sucesso: Garante que a opção '1' retorna a estratégia BeginnerStrategy."""
        estrategia = RebalanceStrategyFactory.criar_estrategia("1")
        self.assertIsInstance(estrategia, BeginnerStrategy)

    def test_factory_falha_opcao_invalida(self):
        """Cenário de Falha/Exceção: Garante que strings inválidas lançam ValueError."""
        with self.assertRaises(ValueError) as contexto:
            RebalanceStrategyFactory.criar_estrategia("99")
        self.assertIn("Opção de perfil inválida", str(contexto.exception))

    def test_factory_borda_input_vazio(self):
        """Cenário de Borda: Garante que uma string vazia ou espaços em branco também lançam exceção."""
        with self.assertRaises(ValueError):
            RebalanceStrategyFactory.criar_estrategia("")
        with self.assertRaises(ValueError):
            RebalanceStrategyFactory.criar_estrategia(" ")


    # =====================================================================
    # CONJUNTO DE TESTES 2: REBALANCECONTEXT (CONTEXTO / STRATEGY)
    # =====================================================================

    def test_context_sucesso_calculo_rampa(self):
        """Cenário de Sucesso: Garante que o cálculo gera a projeção com os meses corretos."""
        orcamento = Orcamento(renda=4000.0, essencial=2000.0, lazer=1800.0, investimento=200.0)
        metas = {"essencial": 50.0, "lazer": 30.0, "investimento": 20.0}
        
        contexto = RebalanceContext()
        contexto.definir_estrategia(BeginnerStrategy())
        
        resultado = contexto.executar_planejamento(orcamento, metas)
        
        # Validações do sucesso
        self.assertEqual(len(resultado), 3)  # BeginnerStrategy gera 3 meses
        self.assertEqual(resultado[0]["mes"], 1)
        self.assertEqual(resultado[-1]["mes"], 3)

    def test_context_falha_sem_estrategia(self):
        """Cenário de Falha/Exceção: Tentar executar o planejamento sem definir uma estratégia deve lançar ValueError."""
        orcamento = Orcamento(renda=4000.0, essencial=2000.0, lazer=1800.0, investimento=200.0)
        metas = {"essencial": 50.0, "lazer": 30.0, "investimento": 20.0}
        
        contexto = RebalanceContext()
        # Propositadamente NÃO chamamos definir_estrategia()
        
        with self.assertRaises(ValueError) as ctx:
            contexto.executar_planejamento(orcamento, metas)
        self.assertIn("Nenhuma estratégia de reequilíbrio foi definida", str(ctx.exception))

    def test_context_borda_investimento_no_teto(self):
        """Cenário de Borda: Usuário já está na meta ideal de investimentos (ex: 20%)."""
        # Se ele já está na meta, a diferença é 0. O sistema deve manter estável sem quebrar.
        orcamento = Orcamento(renda=1000.0, essencial=500.0, lazer=300.0, investimento=200.0) # 20%
        metas = {"essencial": 50.0, "lazer": 30.0, "investimento": 20.0}
        
        contexto = RebalanceContext()
        contexto.definir_estrategia(InvestorStrategy())
        
        resultado = contexto.executar_planejamento(orcamento, metas)
        
        # No último mês do plano, o investimento deve continuar exatamente em 20% (sem alterações bruscas ou divisões por zero)
        self.assertEqual(resultado[-1]["investimento"], 20.0)

if __name__ == "__main__":
    unittest.main()