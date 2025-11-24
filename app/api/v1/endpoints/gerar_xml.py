from fastapi import APIRouter, Depends, Response
from app.application.schemas.gerar_xml_response_schema import ROCDomainSchema
from app.application.enums.tipo_documento_enum import TipoDocumentoEnum
from app.application.use_cases.gerar_xml_use_case import GerarXMLUseCase
from app.infrastructure.services.xml_service import XMLService

router = APIRouter()

def get_gerar_xml_use_case():
    xml_service = XMLService()
    return GerarXMLUseCase(xml_service=xml_service)

@router.post(
    "/xml",
    summary="Gerar XML a partir de um cálculo",
    description="Recebe os dados de um cálculo e o tipo de documento, e retorna o XML correspondente."
)
async def gerar_xml(
    # O corpo da requisição é o schema de resposta do cálculo
    dados_roc: ROCDomainSchema,
    # O parâmetro da query string é o Enum
    tipo: TipoDocumentoEnum,
    use_case: GerarXMLUseCase = Depends(get_gerar_xml_use_case)
):
    """
    Endpoint que gera um XML.
    """
    # Chama o use case para obter o conteúdo XML
    xml_content = await use_case.execute(dados_roc, tipo)

    # Retorna o conteúdo XML com o media type correto
    return Response(content=xml_content, media_type="application/xml")