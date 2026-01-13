from fastapi import APIRouter, Depends, Response, Body
from app.application.schemas.gerar_xml_response_schema import ROCDomainSchema
from app.application.enums.tipo_documento_enum import TipoDocumentoEnum
from app.application.use_cases.gerar_xml_use_case import GerarXMLUseCase
from app.infrastructure.services.xml_service import XMLService
from app.application.enums.tipo_documento_enum import TipoDocumentoEnum
from app.application.enums.subtipo_documento_enum import SubtipoDocumentoEnum
from app.application.use_cases.validar_xml_use_case import ValidarXMLUseCase
from app.infrastructure.services.validar_xml_service import ValidateXMLService

router = APIRouter()

def get_gerar_xml_use_case():
    xml_service = XMLService()
    return GerarXMLUseCase(xml_service=xml_service)

@router.post(
    "/gerar-xml",
    summary="Gerar XML a partir de um cálculo",
    description="Recebe os dados de um cálculo e o tipo de documento, e retorna o XML correspondente."
)
async def gerar_xml(
    dados_roc: ROCDomainSchema,
    tipo: TipoDocumentoEnum,
    use_case: GerarXMLUseCase = Depends(get_gerar_xml_use_case)
):
    """
    Endpoint que gera um XML.
    """
    # Chama o use case para obter o conteúdo XML
    xml_content = await use_case.execute(dados_roc, tipo)
    return Response(content=xml_content, media_type="application/xml")


def get_validar_xml_use_case():
    validacao_service = ValidateXMLService()
    return ValidarXMLUseCase(validacao_service=validacao_service)

@router.post("/validar-xml", response_model=bool, summary="Valida um XML",
             description="Valida os dados de um documento XML informando o tipo e subtipo")
async def validar_xml(
    tipo: TipoDocumentoEnum,
    subtipo: SubtipoDocumentoEnum,
    
    xml_content: bytes = Body(
        ..., 
        media_type="application/xml", 
        description="Conteúdo do arquivo XML a ser validado."
    ),
    use_case: ValidateXMLService= Depends(get_validar_xml_use_case)
):
    """
    Endpoint que valida um XML.
    """
    # O corpo já vem como bytes, basta decodificar para string
    xml_string = xml_content.decode('utf-8')

    # Chama o use case para validar o XML
    resultado = await use_case.execute(xml_string, tipo, subtipo)
    return resultado



