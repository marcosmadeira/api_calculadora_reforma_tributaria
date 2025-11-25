import httpx
import os
from dotenv import load_dotenv
import logging

from app.application.schemas.gerar_xml_response_schema import ROCDomainSchema
from app.application.schemas.exceptions_schema import ExternalAPIError

load_dotenv()
logger = logging.getLogger(__name__)


class XMLService:
    """
    Serviço de infraestrutura para comunicação com a API de geração de XML.
    """
    BASE_URL = os.getenv('BASE_URL')

    async def gerar_xml(self, dados_roc: ROCDomainSchema, tipo_documento: str) -> str:
        """
        Faz a requisição POST para o endpoint de geração de XML.
        """
        endpoint = f"{self.BASE_URL}/calculadora/xml/generate"
        
        # O Pydantic converte o modelo para um dicionário compatível com JSON
        payload = dados_roc.model_dump(mode='json')

        # Parâmetros da query string
        params = {"tipo": tipo_documento}

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(endpoint, json=payload, params=params)
                response.raise_for_status()
                
                # A resposta é o conteúdo XML bruto (texto)
                xml_content = response.text
                logger.info(f"XML gerado com sucesso para o tipo: {tipo_documento}")
                return xml_content
            
            except httpx.HTTPStatusError as e:
                logger.error(f"Erro na API externa ao gerar XML. Status: {e.response.status_code}")
                logger.error(f"Erro na API externa ao gerar XML. Status: {e}")
                try:
                    error_details = e.response.json()
                except Exception:
                    error_details = {
                        "type": "about:blank",
                        "title": "Erro de comunicação com API Externa",
                        "status": e.response.status_code,
                        "detail": f"A API retornou um erro {e.response.status_code} ao gerar o XML.",
                    }
                raise ExternalAPIError(status_code=e.response.status_code, detail=error_details)
            
            except httpx.RequestError as e:
                logger.error(f'Erro de rede ao tentar se conectar com a API de geração de XML: {e}')
                raise ExternalAPIError(
                    status_code=503,
                    detail={
                        "type": "about:blank",
                        "title": "Serviço Indisponível",
                        "status": 503,
                        "detail": "Não foi possível conectar ao serviço de geração de XML. Tente novamente mais tarde.",
                    }
                )