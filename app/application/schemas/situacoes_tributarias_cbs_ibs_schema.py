from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class SituacaoTributariaSchema(BaseModel):
    # Campos que parecem sempre vir na resposta
    id: int = Field(..., description="ID único da situação tributária")
    codigo: str = Field(..., description="Código da situação tributária")
    descricao: str = Field(..., description="Descrição da situação tributária")
    
    # Campos que são opcionais, pois a API externa não os envia sempre
    tipoAliquota: Optional[str] = Field(None, description="Tipo da alíquota (ex: Padrão)")
    nomenclatura: Optional[str] = Field(None, description="Nomenclatura associada (NBS ou NCM)")
    descricaoTratamentoTributario: Optional[str] = Field(None, description="Descrição do tratamento tributário")
    incompativelComSuspensao: Optional[bool] = Field(None, description="Indica se é incompatível com suspensão")
    exigeGrupoDesoneracao: Optional[bool] = Field(None, description="Indica se exige grupo de desoneração")
    possuiPercentualReducao: Optional[bool] = Field(None, description="Indica se possui percentual de redução")
    indicaApropriacaoCreditoAdquirenteCbs: Optional[bool] = Field(None, description="Indica apropriação de crédito CBS para o adquirente")
    indicaApropriacaoCreditoAdquirenteIbs: Optional[bool] = Field(None, description="Indica apropriação de crédito IBS para o adquirente")
    indicaCreditoPresumidoFornecedor: Optional[bool] = Field(None, description="Indica crédito presumido para o fornecedor")
    indicaCreditoPresumidoAdquirente: Optional[bool] = Field(None, description="Indica crédito presumido para o adquirente")
    creditoOperacaoAntecedente: Optional[str] = Field(None, description="Manutenção ou não do crédito de operação antecedente")
    percentualReducaoCbs: Optional[float] = Field(None, description="Percentual de redução da CBS")
    percentualReducaoIbsUf: Optional[float] = Field(None, description="Percentual de redução do IBS (UF)")
    percentualReducaoIbsMun: Optional[float] = Field(None, description="Percentual de redução do IBS (Município)")
    tiposDfeClassificacao: Optional[List] = Field(default_factory=list, description="Lista de tipos de DFE para classificação")

    class Config:
        json_schema_extra = {
            "example": [
                {
                    "id": 1,
                    "codigo": "000",
                    "descricao": "Tributação integral"
                },
                {
                    "id": 2,
                    "codigo": "010",
                    "descricao": "Tributação com alíquotas uniformes"
                }
            ]
        }
