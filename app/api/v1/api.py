# Este arquivo agrupa todos os roteadores da versão 1 da API.

from fastapi import APIRouter
from app.api.v1.endpoints import calculo
from app.api.v1.endpoints import gerar_xml


# Importando routeadores dos endpoints
api_router = APIRouter()

api_router.include_router(calculo.router, prefix='/calculo', tags=["Cálculo"])

# Inclui o roteador de geração
api_router.include_router(gerar_xml.router, prefix="/gerar", tags=["Geração de Documentos"])

