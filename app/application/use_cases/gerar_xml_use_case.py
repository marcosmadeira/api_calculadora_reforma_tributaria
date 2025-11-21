from app.application.schemas.calculo_regime_geral_response_schema import ROCDomainSchema
from app.application.enums.tipo_documento_enum import TipoDocumentoEnum
from app.infrastructure.services.xml_service import XMLService

class GerarXMLUseCase:
    def __init__(self, xml_service: XMLService):
        self.xml_service = xml_service

    async def execute(self, dados_roc: ROCDomainSchema, tipo_documento: TipoDocumentoEnum) -> str:
        """
        Executa o fluxo de geração de XML.
        """
        # Chama o serviço de infraestrutura para obter o XML
        xml_content = await self.xml_service.gerar_xml(dados_roc, tipo_documento.value)
        
        return xml_content