from pydantic import BaseModel, Field

class CbsIbsMercadoriasInputSchema(BaseModel):
    valorFornecimento: float = Field(..., descritpion="Valor Fornecimento")
    ajusteValorOperacao: float = Field(..., descritpion="Ajuste do Valor da Operacao")
    juros: float = Field(..., descritpion="Juros")
    multas: float = Field(..., description="Multas")
    acrescimos: float = Field(..., description="Acrescimos")
    encargos: float = Field(..., description="Encargos")
    descontosCondicionais: float = Field(..., description="Descontos Condicionais")
    fretePorDentro: float = Field(..., description="Frete por Dentro")
    outrosTributos: float = Field(..., description="Outros Tributos")
    impostoSeletivo: float = Field(..., description="Imposto Seletivo")
    demaisImportancias: float = Field(..., description="Demais Importancias")
    icms: float = Field(..., description="ICMS")
    iss: float = Field(..., description="ISS")
    pis: float = Field(..., description="PIS")
    cofins: float = Field(..., description="COFINS")
    
    class Config:
        schema_extra = {
            "example": {
                "valorFornecimento": 105,
                "ajusteValorOperacao": 5,
                "juros": 5,
                "multas": 5,
                "acrescimos": 5,
                "encargos": 5,
                "descontosCondicionais": 5,
                "fretePorDentro": 10,
                "outrosTributos": 5,
                "demaisImportancias": 10,
                "icms": 5,
                "iss": 6,
                "pis": 8,
                "cofins": 6,
            }
        }
    
class BaseCalculoCbsIbsResponseSchema(BaseModel):
    baseCalculo: float = Field(..., description="Base de Cálculo para o CBS / IBS")

    class Config:
        schema_extra = {
            "example": {
                "baseCalculo"
            }
        }