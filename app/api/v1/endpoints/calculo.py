# Arquivo para definir os endpoints que receberão os dados
# app/api/v1/endpoints/calculo.py

from fastapi import APIRouter, Depends
from typing import List
from app.application.schemas.transacao_schema import TransacaoSchema
from app.application.schemas.resultado_schema import ResultadoSchema
from app.application.use_cases.calcular_impostos_use_case import CalculadoraImpostosUseCase
from app.application.use_cases.base_calculo_is_mercadoria_use_case import CalcularBaseCalculoIsMercadoriaUseCase, BaseCalculoISMercadoriaInputSchema
from app.application.schemas.base_calculo_is_mercadoria_schema import BaseCalculoIsMercadoriaResponseSchema
from app.application.schemas.cbs_ibs_mercadorias_schema import CbsIbsMercadoriasInputSchema, BaseCalculoCbsIbsResponseSchema
from app.infrastructure.services.tributario_service import TributarioService

from app.application.use_cases.base_calculo_cbs_ibs_mercadoria_use_case import CalcularCbsIbsMercadoriaUseCase
from app.application.use_cases.calculo_regime_geral_use_case import CalcularRegimeGeralUseCase
from app.application.schemas.calculo_regime_geral_request_schema import OperacaoInputSchema
from app.application.schemas.calculo_regime_geral_response_schema import ROCDomainSchema



# from app.application.use_cases.base_calculo_cbs_ibs_mercadoria_use_case import 

router = APIRouter()

# Injeção de Dependênci: O FastAPI vai criar uma instância do nosso caso de uso 
# def get_calcular_impostos_use_case():
#     return CalculadoraImpostosUseCase()

# @router.post("/impostos", response_model=ResultadoSchema)
# async def calcular_impostos(
#         transacoes: List[TransacaoSchema],
#         use_case: CalculadoraImpostosUseCase = Depends(get_calcular_impostos_use_case)
# ):
#     """
#     Recebe uma lista de transações e calcula os valores de IBS e CBS.
#     """
#     # Chama o caso de uso para executar a lógica de negócio
#     resultado = use_case.execute(transacoes)

#     return resultado

################## ENDPOINT IS MERCADORIA ########################

def get_calcular_base_calculo_use_case():
    # Injeta o servico de infraestrutura no use case
    tributario_service = TributarioService()
    return CalcularBaseCalculoIsMercadoriaUseCase(tributario_service=tributario_service)

@router.post("/base-calculo/is-mercadorias", response_model=BaseCalculoIsMercadoriaResponseSchema,
             summary="Calcular Base de Cálculo de IS para Mercadorias",
             description='Envia os dados para API oficial da Receita Federal para retornar a base de cálculo')
async def calcular_base_is_mercadorias(dados_input: BaseCalculoISMercadoriaInputSchema,
                                       use_case: CalcularBaseCalculoIsMercadoriaUseCase = Depends(get_calcular_base_calculo_use_case)):
    """
    Endpoint que consome a API de cálculo de base de IS para mercadorias
    """
    resultado = await use_case.execute(dados_input)
    return resultado


################## ENDPOINT CBS IBS MERCADORIA ########################
def get_calcular_base_calculo_cbs_ibs_use_case():
    # Injeta o servico de infraestrutura no use case
    tributario_service = TributarioService()
    return CalcularCbsIbsMercadoriaUseCase(tributario_service=tributario_service)



@router.post("/base-calculo/cbs-ibs-mercadorias", response_model=BaseCalculoCbsIbsResponseSchema,
             summary="Calcular Base de Cálculo de CBS IBS para Mercadorias",
             description='Envia os dados para API oficial da Receita Federal para retornar a base de cálculo')
async def calcular_base_is_mercadorias(dados_input: CbsIbsMercadoriasInputSchema,
                                       use_case: CalcularCbsIbsMercadoriaUseCase = Depends(get_calcular_base_calculo_cbs_ibs_use_case)):
    """
    Endpoint que consome a API de cálculo de base de IS para mercadorias
    """
    resultado = await use_case.execute(dados_input)
    return resultado



# --- Endpoint para calculo do regime geral (calculo completo)
def get_calcular_regime_geral_use_case():
    tribut_service = TributarioService()
    return CalcularRegimeGeralUseCase(tributario_service=tribut_service)


@router.post("/base-calculo/regime-geral", response_model=ROCDomainSchema,
             summary="Calcula os tributos a partir dos dados de uma operação de consumo",
             description="Envia os dados para API oficial da Receita Federal para retornar os valores de tributos")
async def calcular_regime_geral(dados_input: OperacaoInputSchema,
                                use_case: CalcularRegimeGeralUseCase = Depends(get_calcular_regime_geral_use_case)):
    """
    Endpoint que recebe uma operação completa e retorna o cálculo detalhado
    """

    result = await use_case.execute(dados_input)
    return result
