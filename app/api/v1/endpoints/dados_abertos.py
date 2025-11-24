from fastapi import APIRouter, Depends, Query
from datetime import date
from typing import List

from app.application.schemas.situacoes_tributarias_cbs_ibs_schema import SituacaoTributariaSchema
from app.application.use_cases.listar_situacoes_tributarias_cbs_ibs_use_case import ListarSituacoesTributariasUseCase
from app.infrastructure.services.situacoes_tributarias_cbs_ibs_service import SituacaoTributariaService


router = APIRouter()

def get_listar_situacoes_tributarias_use_case():
    dados_abertos_service = SituacaoTributariaService()
    return ListarSituacoesTributariasUseCase(dados=dados_abertos_service)

@router.get(
    "/situacoes-tributarias/cbs-ibs",
    response_model=List[SituacaoTributariaSchema],
    summary="Listar Situações Tributárias (CBS/IBS)",
    description="Obtém a lista das situações tributárias cadastradas vigentes em uma determinada data para CBS/IBS."
)
async def listar_situacoes_tributarias(
    # Parâmetro da query string
    data: date = Query(..., example="2026-01-01", description="Data no padrão ISO 8601 (yyyy-MM-dd)"),
    use_case: ListarSituacoesTributariasUseCase = Depends(get_listar_situacoes_tributarias_use_case)
):
    """
    Endpoint que lista as situações tributárias.
    """
    # Chama o use case para obter a lista de situações tributárias
    resultado = await use_case.execute(data)
    return resultado