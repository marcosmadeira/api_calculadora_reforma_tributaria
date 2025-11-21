# Define como o resultado do cálculo será devolvido pela API.
from pydantic import BaseModel

class ResultadoSchema(BaseModel):
    valor_total_faturado: float
    valor_ibs: float
    valor_cbs: float
    valor_total_impostos: float

    class Config:
        schema_extra = {
            "example": {
                "valor_total_faturado": 150.75,
                "valor_ibs": 7.53,
                "valor_cbs": 4.52,
                "valor_total_impostos": 12.05
            }
        }
