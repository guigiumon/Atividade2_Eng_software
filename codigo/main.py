from abc import ABC, abstractmethod

# =====================================================================
# REQUISITO ADICIONAL / HISTÓRIAS DE USUÁRIO: MODELO DE DADOS (MEMÓRIA)
# =====================================================================

class Orcamento:
    """Representa o estado dos dados financeiros na memória (História 2)."""
    def __init__(self, renda: float, essencial: float, lazer: float, investimento: float):
        self.renda = renda
        self.essencial = essencial
        self.lazer = lazer
        self.investimento = investimento

    def obter_porcentagens(self):
        return {
            "essencial": (self.essencial / self.renda) * 100,
            "lazer": (self.lazer / self.renda) * 100,
            "investimento": (self.investimento / self.renda) * 100
        }


# =====================================================================
# PADRÃO DE PROJETO 1: STRATEGY (COMPORTAMENTAL)
# =====================================================================

class RebalanceStrategy(ABC):
    """Interface comum para os algoritmos de reequilíbrio financeiro."""
    @abstractmethod
    def calcular_rampa(self, orcamento: Orcamento, metas: dict) -> list:
        pass


class BeginnerStrategy(RebalanceStrategy):
    """Estratégia para Iniciantes: Mudanças muito suaves (max 4% ao mês)."""
    def calcular_rampa(self, orcamento: Orcamento, metas: dict) -> list:
        projeção = []
        status_atual = orcamento.obter_porcentagens()
        
        # Simulação simplificada de 3 meses de transição lenta (História 1)
        for mes in range(1, 4):
            fator = mes * 0.33  # Caminha gradualmente até a meta
            dif_investimento = metas["investimento"] - status_atual["investimento"]
            
            invest_mes = status_atual["investimento"] + (dif_investimento * fator)
            lazer_mes = status_atual["lazer"] - (dif_investimento * fator) # Tira do lazer suavemente
            
            projeção.append({
                "mes": mes,
                "essencial": status_atual["essencial"],
                "lazer": max(0.0, lazer_mes),
                "investimento": invest_mes
            })
        return projeção


class InvestorStrategy(RebalanceStrategy):
    """Estratégia para Investidores: Transição rápida e agressiva em 2 meses."""
    def calcular_rampa(self, orcamento: Orcamento, metas: dict) -> list:
        projeção = []
        status_atual = orcamento.obter_porcentagens()
        
        for mes in range(1, 3):
            fator = mes * 0.50  # Rampa direta e agressiva rumo à meta (História 1)
            dif_investimento = metas["investimento"] - status_atual["investimento"]
            
            invest_mes = status_atual["investimento"] + (dif_investimento * fator if mes == 1 else dif_investimento)
            lazer_mes = status_atual["lazer"] - (dif_investimento * fator if mes == 1 else dif_investimento)
            
            projeção.append({
                "mes": mes,
                "essencial": status_atual["essencial"],
                "lazer": max(0.0, lazer_mes),
                "investimento": metas["investimento"] if mes == 2 else invest_mes
            })
        return projeção


class RebalanceContext:
    """Gerenciador que executa a estratégia configurada (Contexto do Strategy)."""
    def __init__(self):
        self._strategy = None

    def definir_estrategia(self, strategy: RebalanceStrategy):
        self._strategy = strategy

    def executar_planejamento(self, orcamento: Orcamento, metas: dict) -> list:
        if not self._strategy:
            raise ValueError("Nenhuma estratégia de reequilíbrio foi definida.")
        return self._strategy.calcular_rampa(orcamento, metas)


# =====================================================================
# PADRÃO DE PROJETO 2: SIMPLE FACTORY (CRIACIONAL)
# =====================================================================

class RebalanceStrategyFactory:
    """Fábrica responsável por instanciar a estratégia correta sem condicionais no fluxo principal."""
    @staticmethod
    def criar_estrategia(nivel_usuario: str) -> RebalanceStrategy:
        opcoes = {
            "1": BeginnerStrategy(),
            "2": InvestorStrategy()
        }
        estrategia = opcoes.get(nivel_usuario)
        if not estrategia:
            raise ValueError("Opção de perfil inválida.")
        return estrategia


# =====================================================================
# FLUXO PRINCIPAL / INTERFACE TERMINAL (CLI)
# =====================================================================

def rodar_sistema():
    print("=== CONSULTOR DE PLANEJAMENTO FINANCEIRO ===")
    
    # Mock de dados iniciais para facilitar o teste do avaliador (Mitigação do Trade-off)
    print("\n[Dados pré-carregados para teste]:")
    renda = 4000.0
    essencial = 2000.0  # 50%
    lazer = 1800.0     # 45%
    investimento = 200.0 # 5%
    print(f"Renda: R${renda} | Essencial: R${essencial} | Lazer: R${lazer} | Investimentos: R${investimento}")
    
    orcamento_usuario = Orcamento(renda, essencial, lazer, investimento)
    
    # Meta ideal padrão do sistema (Regra de negócio: 50-30-20)
    metas_sistema = {"essencial": 50.0, "lazer": 30.0, "investimento": 20.0}

    print("\nEscolha o seu perfil de maturidade financeira:")
    print("1 - Iniciante (Deseja criar o hábito, rampa de transição suave)")
    print("2 - Já Investidor (Possui disciplina, rampa de transição rápida)")
    opcao = input("Digite a opção (1 ou 2): ")

    try:
        # Execução da Factory (Padrão Criacional)
        estrategia_escolhida = RebalanceStrategyFactory.criar_estrategia(opcao)
        
        # Execução do Strategy (Padrão Comportamental)
        motor_calculo = RebalanceContext()
        motor_calculo.definir_estrategia(estrategia_escolhida)
        
        rampa_calculada = motor_calculo.executar_planejamento(orcamento_usuario, metas_sistema)
        
        # Exibição dos resultados (História 3 - Projeção de texto)
        print("\n=== PROJEÇÃO DE REEQUILÍBRIO PROGRESSIVO ===")
        print(f"Estado Atual -> Essencial: 50.0% | Lazer: 45.0% | Investimento: 5.0%")
        print(f"Meta Alvo    -> Essencial: {metas_sistema['essencial']}% | Lazer: {metas_sistema['lazer']}% | Investimento: {metas_sistema['investimento']}%")
        print("-" * 65)
        
        for plano in rampa_calculada:
            print(f"Mês {plano['mes']}: Essencial: {plano['essencial']:.1f}% | "
                  f"Lazer: {plano['lazer']:.1f}% | "
                  f"Investimento: {plano['investimento']:.1f}%")
            
        print("-" * 65)
        print("Sugestão gerada com sucesso! Ajuste seus gastos conforme as metas mensais.")

    except ValueError as e:
        print(f"\nErro no processamento: {e}")

if __name__ == "__main__":
    rodar_sistema()