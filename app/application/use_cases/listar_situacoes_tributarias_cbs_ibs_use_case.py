from datetime import date
from app.infrastructure.services.situacoes_tributarias_cbs_ibs_service import SituacaoTributariaService

class ListarSituacoesTributariasUseCase:
    def __init__(self, dados: SituacaoTributariaService):
        self.dados = dados


    async def execute(self, data_consulta: date) -> list:
        """
        Executa o fluxo de listagem de situacoes tributarias ibs cbs
        """
        resultado_lista = await self.dados.listar_situacoes_tributarias_cbs_ibs(data_consulta)
        return resultado_lista
