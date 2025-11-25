from app.application.enums.tipo_documento_enum import TipoDocumentoEnum
from app.application.enums.subtipo_documento_enum import SubtipoDocumentoEnum
from app.infrastructure.services.validar_xml_service import ValidateXMLService

class ValidarXMLUseCase:
    def __init__(self, validacao_service: ValidateXMLService):
        self.validacao_service = validacao_service

    async def execute(self, xml_content: str, tipo: TipoDocumentoEnum, subtipo: SubtipoDocumentoEnum) -> bool:
        """
        Executa o fluxo de validacao do XML
        """
        # Chama o servico de infraestrutura para obter o resultado da validacao
        resultado = await self.validacao_service.validar_xml_service(xml_content, tipo.value, subtipo.value)
        return resultado
        
        