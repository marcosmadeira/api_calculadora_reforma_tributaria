from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime



class BuscaRegimeTributarioRequestSchema(BaseModel):
    cnpj: str = Field(
        ..., 
        min_length=8,  # Garante que tenha no mínimo 8 caracteres
        max_length=8,  # Garante que tenha no máximo 8 caracteres
        pattern="^\d{8}$", # Expressão regular: ^ (início) \d{8} (exatamente 8 dígitos) $ (fim)
        description="Raiz do CNPJ (8 primeiros dígitos numéricos)"
    )