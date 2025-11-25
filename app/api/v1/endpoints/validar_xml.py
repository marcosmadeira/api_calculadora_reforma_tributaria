from fastapi import APIRouter, Depends, Request
from app.application.enums.tipo_documento_enum import TipoDocumentoEnum
from app.application.enums.subtipo_documento_enum import SubtipoDocumentoEnum
from app.application.use_case_validar_xml_use_case import ValidarXMLUseCase
from app.infrastructure.services.validar_xml_service import ValidateXMLService


router =  APIRouter()

def get_validar_xml_use_case():
    validacao_service = ValidateXMLService
    return ValidarXMLUseCase(validacao_service=validacao_service)

@router.post("/xml", response_mode=bool, summary="Valida um XML",
             description="Valida os dados de um documento XML informando o tipo e subtipo")
async def validar_xml(
    # Injeta o objeto Request para acessar o corpo bruto
    request: Request,
    # Parametros da query string sao validados como Enums
    tipo: TipoDocumentoEnum,
    subtipo: SubtipoDocumentoEnum,
    use_case: ValidarXMLUseCase = Depends(get_validar_xml_use_case)
):
    """
    Endpoint que valida um XML
    """
    # Lê o corpo da requisicao (string de bytes) e decodifica para string
    xml_content_bytes = await request.body()
    xml_string = xml_content_bytes.decode('utf-8')

    # Chama o use case para validar o XML
    resultado = await use_case.execute(xml_string, tipo, subtipo)
    return resultado

