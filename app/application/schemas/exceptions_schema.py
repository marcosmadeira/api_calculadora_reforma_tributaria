# app/api/exceptions.py
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, Optional

class ProblemDetailSchema(BaseModel):
    """
    Modelo Pydantic para respostas de erros de requisições
    """
    type: Optional[str] = None
    title: Optional[str] = None
    status: int
    detail: Optional[str] = None
    instance: Optional[str] = None
    properties: Optional[Dict[str, Any]] = None


class ExternalAPIError(HTTPException):
    """
    Excecao customizada para erros retornados por apis externas 
    """
    def __init__(self, status_code: int, detail: Dict[str, Any]):
        # Passa os detalhes para a classe pai
        super().__init__(status_code=status_code, detail=detail)


async def external_api_exception_handler(request: Request, exc: ExternalAPIError):
    """
    Transforma a ExternalAPIError em uma resposta JSON formatada
    """
    # O status_code será o da API externa(400, 404, 422, etc)
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail
    )
