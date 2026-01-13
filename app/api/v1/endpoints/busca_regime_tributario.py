# app/api/v1/endpoints/busca_regime_tributario.py

from fastapi import APIRouter, Depends, Query, Request
from datetime import date
from typing import List
from app.application.schemas.busca_regime_tributario_request_schema import BuscaRegimeTributarioRequestSchema
from app.application.schemas.busca_regime_tributario_response_schema import BuscaRegimeTributarioResponseSchema # <-- Lembre-se desta importação!
from app.application.use_cases.busca_regime_tributario_use_case import BuscaRegimeTributarioUseCase
from app.infrastructure.services.busca_regime_tributario_service import BuscaRegimeTributarioService

from fastapi import Request

router = APIRouter()

# Nova função de dependência que obtém o serviço a partir do estado da aplicação
def get_busca_regime_tributario_service(request: Request):
    return request.app.state.busca_regime_service

def get_busca_regime_tributario_use_case(
    # Agora a dependência é o serviço compartilhado
    service: BuscaRegimeTributarioService = Depends(get_busca_regime_tributario_service)
):
    # Apenas cria o use case, sem recarregar o serviço
    return BuscaRegimeTributarioUseCase(service)

async def get_busca_regime_request(
    cnpj: str = Query(..., example="11115518", description="Raiz do CNPJ (8 primeiros dígitos)")
) -> BuscaRegimeTributarioRequestSchema:
    """
    Dependência que lê a query string 'cnpj' e a valida
    usando o Pydantic. Se a validação falhar, o FastAPI
    retorna um erro 422 automaticamente.
    """
    return BuscaRegimeTributarioRequestSchema(cnpj=cnpj)



@router.get(
    "/busca-regime-tributario",
    response_model=BuscaRegimeTributarioResponseSchema,
    summary="Buscar Regime Tributário",
    description="Obtém o regime tributário vigente para um contribuinte.",
    tags=["Regime Tributário"] # Adicionei uma tag para organização no Swagger
)
async def buscar_regime_tributario(
    cnpj: str = Query(..., example="23456789000123", description="CNPJ do contribuinte"),
    use_case: BuscaRegimeTributarioUseCase = Depends(get_busca_regime_tributario_use_case)
):
    """
    Endpoint que busca o regime tributário.
    """
    request_schema = BuscaRegimeTributarioRequestSchema(cnpj=cnpj)
    resultado = await use_case.execute(request_schema)
    return resultado



@router.get(
    "/debug/parquet-preview",
    tags=["Debug"], # Cria uma seção "Debug" no Swagger
    summary="Visualiza as primeiras linhas do arquivo Parquet (Apenas Dev!)",
    include_in_schema=False # <-- IMPORTANTE: Isso esconde o endpoint do Swagger/OpenAPI por padrão
                            # Mude para True se quiser vê-lo no Swagger durante o dev
)


async def buscar_regime_tributario(
    # O endpoint agora depende da função de validação
    request: BuscaRegimeTributarioRequestSchema = Depends(get_busca_regime_request),
    use_case: BuscaRegimeTributarioUseCase = Depends(get_busca_regime_tributario_use_case)
):
    """
    Endpoint que busca o regime tributário.
    """
    resultado = await use_case.execute(request)
    return resultado