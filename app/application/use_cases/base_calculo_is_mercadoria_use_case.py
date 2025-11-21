# app/application/use_case_calcular_base_calculo_use_case.py
from app.application.schemas.base_calculo_is_mercadoria_schema import (
    BaseCalculoISMercadoriaInputSchema,
    BaseCalculoIsMercadoriaResponseSchema
    )
from app.infrastructure.services.tributario_service import TributarioService


class CalcularBaseCalculoIsMercadoriaUseCase:
    def __init__(self, tributario_service: TributarioService):
        self.tributario_service = tributario_service

    async def execute(self, dados_input: BaseCalculoISMercadoriaInputSchema) -> BaseCalculoIsMercadoriaResponseSchema:
        """
        Executa o fluxo de calculo da base de cálculo
        """
        # Chama o servico de infra para obter o resultado da api externa (Calculadora Reforma Tributária)
        resultado_dict = await self.tributario_service.calcular_base_is_mercadorias(dados_input)

        # Valida e formata o resultado usando o schema de resposta
        resultado_schema = BaseCalculoIsMercadoriaResponseSchema(**resultado_dict)

        return resultado_schema
        

