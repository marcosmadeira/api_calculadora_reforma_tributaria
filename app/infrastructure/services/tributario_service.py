# app/infrastructure/services/tributario_service.py
# Arquivo responsável por montar as requisições a api da Calculadora da Reforma Tributária
import httpx
from app.application.schemas.base_calculo_is_mercadoria_schema import BaseCalculoISMercadoriaInputSchema
from app.application.schemas.cbs_ibs_mercadorias_schema import CbsIbsMercadoriasInputSchema
from app.application.schemas.exceptions_schema import ExternalAPIError
from app.application.schemas.calculo_regime_geral_request_schema import OperacaoInputSchema
import os
from dotenv import load_dotenv
import logging


# Carrega as variáveis de ambiente
load_dotenv()

# Configure um logger para este módulo específico
logger = logging.getLogger(__name__)


class TributarioService:
    """
    Serviço de infraestrutura para comunicação com a API de cálculo tributário do governo.
    """
    BASE_URL = os.getenv('BASE_URL')

    async def calcular_base_is_mercadorias(self, dados_calculo: BaseCalculoISMercadoriaInputSchema) -> dict:
        """
        Faz a requisição POST para o endpoint de cálculo de base de IS para mercadorias.
        """
        endpoint = f"{self.BASE_URL}/calculadora/base-calculo/is-mercadorias"

        # Converte o modelo para um dicionariao e o httpx converte para JSON
        payload = dados_calculo.dict()

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(endpoint, json=payload)
                # Lança exceção se for uma resposta 400 ou 500
                response.raise_for_status()
                resultado = response.json()

                # Pega o valor da base de calculo ou None se não existir
                base_calculo_valor = resultado.get('baseCalculo')
                if base_calculo_valor is not None:
                    logger.info(f"Base cálculo IS (Mercadoria) retornado: {base_calculo_valor}")
                    return resultado
                else:
                    logger.warning(f'A API retorno sucesso status code 200 mas a chave "baseCalculo" não foi localizada na resposta')
                    return resultado
            
            except httpx.HTTPStatusError as e:
                try:
                    error_details = e.response.json()
                except Exception:
                    # Se a resposta não for um json, cria um erro generico
                    error_details = {
                        "type": "about:blank",
                        "title": "Erro de comunicação com API Externa",
                        "status": e.response.status_code,
                        "detail": f"A API retornou um erro {e.response.status_code} sem detalhes no corpo da resposta",
                        "instance": str(e.request.url)
                    }
                    
                raise ExternalAPIError(
                    status_code=e.response.status_code,
                    detail=error_details
                )
            
            except httpx.RequestError as error:
                logger.error(f'Erro na requisição para calcular base IS Mercadorias: {error}')
                # Propagar exceção para que camada superiro possa trata-la
                raise ExternalAPIError(
                    status_code=503,
                    detail={
                        "type": "about.blank",
                        "title": "Serviço Indisponível",
                        "status": 503,
                        "detail": "Não foi possível conectar ao serviço de cálculo tributário. Tente novamente mais tarde.",
                        "instance": str(e.request.url)
                    }
                )

    async def calcular_base_cbs_ibs_mercadorias(self, dados_calculo: CbsIbsMercadoriasInputSchema) -> dict:
        """
        Faz a requisição POST para o endpoint de calculo de base de CBS e IBS para mercadorias
        """

        endpoint = f"{self.BASE_URL}/calculadora/base-calculo/cbs-ibs-mercadorias"

        payload = dados_calculo.dict()

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(endpoint, json=payload)
                # Lança exceção se for uma resposta 400 ou 500
                response.raise_for_status()
                resultado = response.json()

                # Pega o valor da base de calculo ou None se não existir
                base_calculo_valor = resultado.get('baseCalculo')
                if base_calculo_valor is not None:
                    logger.info(f"Base cálculo CBS/IBS (Mercadorias) retornado: {base_calculo_valor}")
                    return resultado
                else:
                    logger.warning(f'A API retorno sucesso status code 200 mas a chave "baseCalculo" não foi localizada na resposta')
                    return resultado
            
            except httpx.HTTPStatusError as e:
                try:
                    error_details = e.response.json()
                except Exception:
                    # Se a resposta não for um json, cria um erro generico
                    error_details = {
                        "type": "about:blank",
                        "title": "Erro de comunicação com API Externa",
                        "status": e.response.status_code,
                        "detail": f"A API retornou um erro {e.response.status_code} sem detalhes no corpo da resposta",
                        "instance": str(e.request.url)
                    }
                    
                raise ExternalAPIError(
                    status_code=e.response.status_code,
                    detail=error_details
                )
            
            except httpx.RequestError as error:
                logger.error(f'Erro na requisição para calcular base IS Mercadorias: {error}')
                # Propagar exceção para que camada superiro possa trata-la
                raise ExternalAPIError(
                    status_code=503,
                    detail={
                        "type": "about.blank",
                        "title": "Serviço Indisponível",
                        "status": 503,
                        "detail": "Não foi possível conectar ao serviço de cálculo tributário. Tente novamente mais tarde.",
                        "instance": str(e.request.url)
                    }
                )
            
    
    async def calcular_regime_geral(self, dados_calculo: OperacaoInputSchema) -> dict:
        """
        Faz a requisição POST para o endpoint de calculo dos tributos IS CBS IBS para operações
        de consumo
        """

        endpoint = f"{self.BASE_URL}/calculadora/regime-geral"

        payload = dados_calculo.model_dump(mode="json")

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(endpoint, json=payload)
                response.raise_for_status() 
                
                resultado = response.json()

                # --- VERIFICAÇÃO E TRATAMENTO COMPLETOS ---
                # Garante que a API externa não retornou um corpo vazio ou nulo
                if not isinstance(resultado, dict):
                    logger.warning(f"A API externa retornou 200 OK, mas a resposta não é um JSON válido: {resultado}")
                    # Lança uma exceção para interromper o fluxo e ser tratada pelo manipulador global
                    raise ExternalAPIError(
                        status_code=502, # 502 Bad Gateway é um código apropriado aqui
                        detail={
                            "type": "about:blank",
                            "title": "Resposta Inválida da API Externa",
                            "status": 502,
                            "detail": "O serviço de cálculo retornou uma resposta vazia ou em formato inesperado.",
                            "instance": endpoint
                        }
                    )
                
                logger.info(f"Cálculo de regime geral realizado com sucesso para a operação ID: {dados_calculo.id}")
                return resultado
            
            except httpx.HTTPStatusError as e:
                # ... (seu bloco except para HTTPStatusError está correto) ...
                try:
                    error_details = e.response.json()
                except Exception:
                    error_details = {
                        "type": "about:blank",
                        "title": "Erro de comunicação com API Externa",
                        "status": e.response.status_code,
                        "detail": f"A API retornou um erro {e.response.status_code} sem detalhes no corpo da resposta",
                        "instance": str(e.request.url)
                    }
                raise ExternalAPIError(status_code=e.response.status_code, detail=error_details)
            
            except httpx.RequestError as error:
                # ... (seu bloco except para RequestError está correto) ...
                logger.error(f'Erro na requisição para calcular Regime Geral: {error}')
                raise ExternalAPIError(
                    status_code=503,
                    detail={
                        "type": "about.blank",
                        "title": "Serviço Indisponível",
                        "status": 503,
                        "detail": "Não foi possível conectar ao serviço de cálculo tributário. Tente novamente mais tarde.",
                        "instance": str(error.request.url)
                    }
                )