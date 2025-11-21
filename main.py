# main.py
from fastapi import FastAPI
from app.api.v1.api import api_router
from app.application.schemas.exceptions_schema import ExternalAPIError, external_api_exception_handler
import logging

# Configura o nível de log para INFO e define um formato simples para as mensagens
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

app = FastAPI(
    title="API Calculadora ",
    description="API para calcular impostos baseados na Reforma Tributária (IBS e CBS).",
    version="1.0.0",
)

# Registra o manipulador de excecoes globais que definimos
app.add_exception_handler(ExternalAPIError, external_api_exception_handler)

# Inclui as rotas da versão 1 da API
app.include_router(api_router, prefix="/api/v1")

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API de Cálculo Tributário. Acesse /docs para a documentação."}