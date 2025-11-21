from app.infrastructure.services.tributario_service import TributarioService
from app.application.schemas.calculo_regime_geral_request_schema import OperacaoInputSchema
from app.application.schemas.calculo_regime_geral_response_schema import ROCDomainSchema
import logging

class CalcularRegimeGeralUseCase:
    def __init__(self, tributario_service: TributarioService):
        self.tributario_service = tributario_service

    async def execute(self, dados_input: OperacaoInputSchema) -> ROCDomainSchema:
        """
        Executa o fluxo de calculo da base de cálculo
        """
        # Chama o servico de infra para obter o resultado da api externa (Calculadora Reforma Tributária)
        resultado_dict = await self.tributario_service.calcular_regime_geral(dados_input)
        logging.warning(f"Resultado Dict enviado foi {resultado_dict}")


        # Valida e formata o resultado usando o schema de resposta
        resultado_schema = ROCDomainSchema(**resultado_dict)

        return resultado_schema