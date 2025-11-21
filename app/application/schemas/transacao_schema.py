# app/application/schemas/transacao_schema.py

from pydantic import BaseModel, Field

class TransacaoSchema(BaseModel):
    valor: float = Field(..., gt=0, description="Valor da transação em Reais (R$).")
    categoria: str = Field(..., description="Categoria da transação (ex: produto, servico)")


    class Config:
        schema_extra = {
            "example": {
                "valor": 150.75,
                "categoria": "produto"
            }
        }



