# Este arquivo agrupa todos os roteadores da versão 1 da API.

from fastapi import APIRouter
from app.api.v1.endpoints import base_de_calculo
from app.api.v1.endpoints import gerar_documentos
from app.api.v1.endpoints import dados_abertos


# Importando routeadores dos endpoints
api_router = APIRouter()

api_router.include_router(base_de_calculo.router, prefix='/calculo', tags=["Base de Cálculo"])

# Inclui o roteador de geração
api_router.include_router(gerar_documentos.router, prefix="/gerar", tags=["Geração de Documentos"])

# Inclui o roteador de dados abertos
api_router.include_router(dados_abertos.router, prefix="/dados-abertos", tags=['Dados Abertos'])


