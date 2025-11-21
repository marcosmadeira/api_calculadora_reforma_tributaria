from typing import List
from app.domain.value_objects.transacao import Transacao
from app.domain.value_objects.resultado import Resultado


# Aliquotas ficticias para exemplo
ALIQUOTA_IBS = 0.05
ALIQUOTA_CBS = 0.03

class CalculadoraService:
    def calcular(self, transacoes: List[Transacao]) -> Resultado:
        if not transacoes:
            return Resultado(0.0, 0.0, 0.0, 0.0)
        
        valor_total = sum(t.valor for t in transacoes)

        # Lógica de negócio simplificada
        # No futuro, pode haver regras diferentes por categoria
        valor_ibs = valor_total * ALIQUOTA_IBS
        valor_cbs = valor_total * ALIQUOTA_CBS
        valor_total_impostos = valor_ibs + valor_cbs

        return Resultado(
            valor_total_faturado=valor_total,
            valor_ibs = valor_ibs,
            valor_cbs = valor_cbs,
            valor_total_impostos=valor_total_impostos
        )


