import os
import logging
import asyncio
import pandas as pd
from app.application.schemas.exceptions_schema import ExternalAPIError

logger = logging.getLogger(__name__)

class BuscaRegimeTributarioService:
    """
    Serviço de infraestrutura para buscar dados de regime tributário em um arquivo Parquet.
    O arquivo é carregado em memória durante a inicialização para buscas rápidas.
    """
    def __init__(self):
        """
        Inicializa o serviço, carregando o arquivo Parquet em um DataFrame do pandas.
        """
        self.parquet_path = os.getenv('PARQUET_FILE_PATH')
        if not self.parquet_path:
            logger.error("A variável de ambiente 'PARQUET_FILE_PATH' não foi definida.")
            raise ValueError("A variável de ambiente 'PARQUET_FILE_PATH' não foi definida.")

        if not os.path.exists(self.parquet_path):
            logger.error(f"O arquivo Parquet não foi encontrado em: {self.parquet_path}")
            raise FileNotFoundError(f"O arquivo de dados não foi encontrado em: {self.parquet_path}")

        try:
            # Carrega o arquivo Parquet para um DataFrame em memória
            self.df = pd.read_parquet(self.parquet_path)
            logger.info(f"Arquivo Parquet '{self.parquet_path}' carregado com sucesso. Total de registros: {len(self.df)}")
        except Exception as e:
            logger.error(f"Erro ao carregar o arquivo Parquet: {e}")
            raise RuntimeError(f"Falha ao carregar o arquivo de dados: {e}")

    def _find_regime_in_dataframe(self, cnpj: str) -> dict:
        """
        Função síncrona (bloqueante) que busca o CNPJ no DataFrame.
        Esta função será executada em uma thread separada.
        """
        # 1. Pega apenas os 8 primeiros dígitos do CNPJ para a busca
        cnpj_str = str(cnpj)
        cnpj_raiz = cnpj_str[:8]
        
        # 2. Filtra o DataFrame pela raiz do CNPJ
        resultado_df = self.df[self.df['cnpj'] == cnpj_raiz]

        if resultado_df.empty:
            raise ExternalAPIError(
                status_code=404,
                detail={
                    "type": "about:blank",
                    "title": "CNPJ não encontrado",
                    "status": 404,
                    "detail": f"O regime tributário para a raiz do CNPJ {cnpj_raiz} não foi encontrado em nossa base de dados.",
                }
            )
        
        row = resultado_df.iloc[0]
        
        # 3. Lida com a coluna 'ano' que pode ser NaN
        ano = row['ano']
        ano_vigente = None
        if not pd.isna(ano):
            # Se não for NaN, converte para inteiro
            ano_vigente = int(ano)
        
        # 4. Retorna o dicionário com os dados
        return {
            "regime_tributario": row['regime'],
            "ano_vigente": ano_vigente # Será um inteiro ou None
        }

    async def buscar_regime_tributario(self, cnpj: str) -> dict:
        """
        Busca o regime tributário para um CNPJ no DataFrame carregado em memória.
        """
        logger.info(f"Iniciando busca de regime tributário para o CNPJ: {cnpj}")
        
        loop = asyncio.get_running_loop()
        try:
            # Executa a função bloqueante em um executor de thread para não travar o event loop
            resultado = await loop.run_in_executor(
                None,  # Usa o executor de thread padrão
                self._find_regime_in_dataframe,
                cnpj
            )
            logger.info(f"Regime tributário encontrado para o CNPJ {cnpj}.")
            return resultado
        except ExternalAPIError:
            # Repassa a exceção de "não encontrado" para o use case
            raise
        except Exception as e:
            logger.error(f"Ocorreu um erro inesperado ao buscar o CNPJ {cnpj}: {e}")
            raise ExternalAPIError(
                status_code=500,
                detail={
                    "type": "about:blank",
                    "title": "Erro Interno do Servidor",
                    "status": 500,
                    "detail": "Ocorreu um erro ao processar sua solicitação.",
                }
            )