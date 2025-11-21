# app/application/schemas/calculo_regime_geral.py
# Contém todos os modelos necessários para construir o corpo da requisição.
# Devido a estrutura de dados da api ser bastante complexa e aninhada, será necessário criar varios modelos Pydantic separados para
# tornar o código organizado e reutilizável

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class ImpostoSeletivoSchema(BaseModel):
    cst: str = Field(..., max_length=3, pattern=r"\d+", description="Codigo da situacao tributaria")
    baseCalculo: float = Field(..., description='Base de calculo do imposto')
    quantidade: float = Field(..., description="Quantidade")
    unidade: str = Field(..., description="Unidade de medida")
    impostoInformado: float = Field(..., description="Imposto seletivo informado pelo contribuinte")
    cClassTrib: str = Field(..., max_length=6, pattern=r"\d+", description="Codigo da classificacao tributaria")


class TributacaoRegularSchema(BaseModel):
    cst: str = Field(..., max_length=3, pattern=r"\d+", description="Codigo da situacao tributaria")
    cClassTrib: str = Field(..., max_length=6, pattern=r"\d+", description="Coda da classificacao tributaria")


class ItemSchema(BaseModel):
    numero: int = Field(..., ge=1, le=9999999, description="Numero do Item")
    ncm: Optional[str] = Field(None, description="Codigo NCM")
    nbs: Optional[str] = Field(None, description="Codigo NBS")
    cst: str = Field(..., max_length=3, pattern=r"\d+", description="Codigo da situacao tributaria")
    baseCalculo: float = Field(..., description="Base de calculo do imposto")
    quantidade: float = Field(..., description="Quantidade")
    unidade: str = Field(..., description="Unidade de medida")
    impostoSeletivo: ImpostoSeletivoSchema
    tributacaoRegular: TributacaoRegularSchema
    cClassTrib: str = Field(..., max_length=6, pattern=r"\d+", description="Codigo de classificacao tributaria")


# --- Modelo Principal da Requisição ---

class OperacaoInputSchema(BaseModel):
    id: str = Field(..., description="Identificador do ROC")
    versao: str = Field(..., description="Versao do ROC")
    dataHoraEmissao: datetime = Field(..., description="Data e hora de emissao do documento no formato UTC")
    municipio: int = Field(..., ge=0, le=9999999, description="Codigo do Municipio (tabela IBGE)")
    uf: str = Field(..., min_length=2, max_length=2, description="Sigla da UF")
    itens: List[ItemSchema] = Field(..., min_items=1, description="Itens da Operacao")


    class Config:
        json_schema_extra = {
            "example": {
                "id": "6194602ea71cbf9431c236de4409d920",
                "versao": "0.0.1",
                "dataHoraEmissao": "2026-01-01T09:50:05-03:00",
                "municipio": 4314902,
                "uf": "RS",
                "itens": [
                    {
                        "numero": 1,
                        "ncm": "24021000",
                        "nbs": "109052100",
                        "cst": "000",
                        "baseCalculo": 200,
                        "quantidade": 1,
                        "unidade": "LT",
                        "impostoSeletivo": {
                            "cst": "000",
                            "baseCalculo": 200,
                            "quantidade": 1,
                            "unidade": "LT",
                            "impostoInformado": 12,
                            "cClassTrib": "000000"
                        },
                        "tributacaoRegular": {
                            "cst": "000",
                            "cClassTrib": "000000"
                        },
                        "cClassTrib": "000001"
                        
                    }
                ]
            }
        }

















