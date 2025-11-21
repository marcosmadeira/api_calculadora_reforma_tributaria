# app/application/use_case_calcular_base_calculo_cbs_ibs_use_case.py
from app.application.schemas.cbs_ibs_mercadorias_schema import (
    CbsIbsMercadoriasInputSchema,
    BaseCalculoCbsIbsResponseSchema 
    )
from app.infrastructure.services.tributario_service import TributarioService
        

class CalcularCbsIbsMercadoriaUseCase:
    def __init__(self, tributario_service=TributarioService):
        self.tributario_service = tributario_service

    async def execute(self, dados_input= CbsIbsMercadoriasInputSchema) -> BaseCalculoCbsIbsResponseSchema:
        """
        Executa o fluxo de calculo da base de calculo da CBS IBS
        """
        # Chama o servico de infra para obter o resultado da api externa (Calculadora Reforma Tributária)
        resultado_dict = await self.tributario_service.calcular_base_cbs_ibs_mercadorias(dados_input)

        # Valida e formata o resultado usando o schema de resposta
        resultado_schema = BaseCalculoCbsIbsResponseSchema(**resultado_dict)

        return resultado_schema
    


