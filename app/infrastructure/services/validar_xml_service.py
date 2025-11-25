import httpx
import os
from dotenv import load_dotenv
import logging
from app.application.schemas.gerar_xml_response_schema import ROCDomainSchema
from app.application.schemas.exceptions_schema import ExternalAPIError


load_dotenv()
logger = logging.getLogger(__name__)

class ValidateXMLService:
    """
    Serviço de infraestrutua para comunicacao com API externa para validar XML gerado
    """

    BASE_URL = os.getenv("BASE_URL")

    async def validar_xml_service(self, xml_content: str, tipo: str, subtipo: str) -> bool:
        """
        Faz a requisição POST para o endpoint de validação do XML
        """
        endpoint = f"{self.BASE_URL}/calculadora/xml/validate"

        params = {"tipo": tipo, "subtipo": subtipo}

        headers = {"Content-Type": "application/xml"}

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(endpoint, content=xml_content, params=params, headers=headers)
                response.raise_for_status()

                resultado = response.json()
                logger.info(f"XML validado com sucesso para o tipo {tipo} e subtipo: {subtipo}")
                return resultado
            except httpx.HTTPStatusError as error:
                logger.error(f"Erro na API externa ao validar XML. Status: {error.response.status_code}")
                try:
                    error_details = error.response.json()
                except Exception:
                    error_details = {
                        "type": "about:blank",
                        "title": "Erro na comunicação com API Externa",
                        "status": error.response.status_code,
                        "detail": f"A API retornou um erro {error.response_status_code} ao validar o XML"
                    }
                raise ExternalAPIError(status_code=error.response.status_code, detail=error_details)
            except httpx.RequestError as e:
                logger.error(f"Erro de rede ao tentar se conectar com a API para validação do XML: {e}")
                raise ExternalAPIError(
                    status_code=503,
                    detail={
                        "type": "about.blank",
                        "title": "Serviço Indisponível",
                        "status": 503,
                        "detail": "Não foi possivel conectar ao serviço de validacao de XML. Tente novamente mais tarde"
                    }
                )
