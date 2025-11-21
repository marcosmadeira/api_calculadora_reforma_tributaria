# Arquivo orquestrador da aplicacao. Pega os dados da API e chama o serviço de domínio para fazer o trabalho pesado:
# app/application/use_cases/calcular_impostos_use_case.py

from typing import List
from app.application.schemas.transacao_schema import TransacaoSchema
from app.application.schemas.resultado_schema import ResultadoSchema
from app.domain.services.calculadora_service import CalculadoraService
from app.domain.value_objects.transacao import Transacao


class CalculadoraImpostosUseCase:
    def __init__(self):
        self.calculadora_service = CalculadoraService()

    def execute(self, transacoes_schema: List[TransacaoSchema]) -> ResultadoSchema:
        # Converte os schemas da API em objetos de valor do domínio
        transacoes_dominio = [
            Transacao(valor=t.valor, categoria=t.categoria) for t in transacoes_schema
        ]

        # Chama o serviço de domínio para realizar o cálculo
        resultado_dominio =self.calculadora_service.calcular(transacoes_dominio)
        
        # Converte o resultado do domínio de volta para o schema da API
        return ResultadoSchema(
            valor_total_faturado = resultado_dominio.valor_total_faturado,
            valor_ibs=resultado_dominio.valor_ibs,
            valor_cbs=resultado_dominio.valor_cbs,
            valor_total_impostos=resultado_dominio.valor_total_impostos)
        



