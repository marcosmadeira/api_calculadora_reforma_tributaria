import httpx
import os
from dotenv import load_dotenv
import logging
from datetime import date
from app.application.schemas.exceptions_schema import ExternalAPIError


load_dotenv()
logger = logging.getLogger(__name__)

class SituacaoTributariaService:
    """
    Servico de infraestrutura para comunicacao com a API externa
    """
    BASE_URL = os.getenv('BASE_URL')

    async def listar_situacoes_tributarias_cbs_ibs(self, data_consulta: date) -> list:
        """
        Faz a requisicao GET para obter a lista de situacoes tributarias
        """
        endpoint = f"{self.BASE_URL}/calculadora/dados-abertos/situacoes-tributarias/cbs-ibs"

        # Parâmetros da query string
        params = {"data": data_consulta.isoformat()} # Formata para o YYYY-DD-MM

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(endpoint, params=params)
                response.raise_for_status()

                resultado = response.json()
                logger.info(f"Consulta de situacoes tributaria para a data {data_consulta.isoformat()} realizada com sucesso")
                return resultado
            
            except httpx.HTTPStatusError as err:
                logger.error(f"Erro na API RT ao consultar situacoes tributarias IBS/CBS. Status {err.response.status_code}")
                try:
                    error_details = err.response.json()
                except Exception:
                    error_details = {
                        "type": "about:blank",
                        "title": "Erro de comunicação com API Externa",
                        "status": e.response.status_code,
                        "detail": f"A API retornou um erro {e.response.status_code} ao consultar os dados.",
                    }
                raise ExternalAPIError(status_code=e.response.status_code, detail=error_details)
            
            except httpx.RequestError as e:
                logger.error(f'Erro de rede ao tentar se conectar com a API de dados abertos: {e}')
                raise ExternalAPIError(
                    status_code=503,
                    detail={
                        "type": "about:blank",
                        "title": "Serviço Indisponível",
                        "status": 503,
                        "detail": "Não foi possível conectar ao serviço de dados abertos. Tente novamente mais tarde.",
                    }
                    )
