# app/application/use_cases/busca_regime_tributario_use_case.py

from app.application.schemas.busca_regime_tributario_response_schema import BuscaRegimeTributarioResponseSchema
from app.infrastructure.services.busca_regime_tributario_service import BuscaRegimeTributarioService
from app.application.schemas.busca_regime_tributario_request_schema import BuscaRegimeTributarioRequestSchema

class BuscaRegimeTributarioUseCase:
    def __init__(self, busca_regime_tributario_service: BuscaRegimeTributarioService):
        self.busca_regime_tributario_service = busca_regime_tributario_service

    async def execute(self, cnpj: BuscaRegimeTributarioRequestSchema) -> BuscaRegimeTributarioResponseSchema:
        """
        Executa o fluxo de busca do regime tributario
        """
        # Chama o servico de infra para obter o resultado da api externa (Calculadora Reforma Tributária)
        resultado_dict = await self.busca_regime_tributario_service.buscar_regime_tributario(cnpj.cnpj)

        # Valida e formata o resultado usando o schema de resposta
        resultado_schema = BuscaRegimeTributarioResponseSchema(**resultado_dict)

        return resultado_schema
