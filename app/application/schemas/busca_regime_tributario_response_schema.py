from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class BuscaRegimeTributarioResponseSchema(BaseModel):
    # Retorna o regime tributario e o ano vigente
    regime_tributario: str = Field(..., description="Regime tributário vigente")
    ano_vigente: Optional[int] = Field(None, description="Ano vigente")