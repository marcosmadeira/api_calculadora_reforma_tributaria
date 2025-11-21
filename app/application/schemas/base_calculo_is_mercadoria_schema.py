# app/application/schemas/base_calculo_schema.py
from pydantic import BaseModel, Field

class BaseCalculoISMercadoriaInputSchema(BaseModel):
    valorIntegralCobrado: float = Field(..., description="Valor Integral Cobrado")
    ajusteValorOperacao: float = Field(..., description="Ajuste do Valor da Operacao")
    juros: float = Field(..., description="Juros")
    multas: float = Field(..., description="Multas")
    acrescimos: float = Field(..., description="Acrescimos")
    encargos: float = Field(..., description="Encargos")
    descontosCondicionais: float = Field(..., description="Descontos Condicionais")
    fretePorDentro: float = Field(..., description="Frete por Dentro")
    outrosTributos: float = Field(..., description="Outros Tributos")
    demaisImportancias: float = Field(..., description="Demais Importancias")
    icms: float = Field(..., description="ICMS")
    iss: float = Field(..., description="ISS")
    pis: float = Field(..., description="PIS")
    cofins: float = Field(..., description="COFINS")
    bonificacao: float = Field(..., description="Bonificacao")
    devolucaoVendas: float = Field(..., description="Devolucao de Vendas")

    class Config:
        schema_extra = {
            "example": {
                "valorIntegralCobrado": 105,
                "ajusteValorOperacao": 5,
                "juros": 5,
                "multas": 5,
                "acrescimos": 5,
                "encargos": 5,
                "descontosCondicionais": 5,
                "fretePorDentro": 5,
                "outrosTributos": 5,
                "demaisImportancias": 5,
                "icms": 5,
                "iss": 5,
                "pis": 5,
                "cofins": 5,
                "bonificacao": 5,
                "devolucaoVendas": 5
            }
        }


class BaseCalculoIsMercadoriaResponseSchema(BaseModel):
    baseCalculo: float = Field(..., description="Base de Calculo calculada pelo servico externo")

    class Config:
        schema_extra = {
            "example": {
                "baseCalculo": 100.55
            }
        }
        





