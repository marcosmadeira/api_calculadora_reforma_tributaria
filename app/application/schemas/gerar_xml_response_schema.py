# app/application/schemas/calculo_regime_response_schema.py

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class GrupoDiferimentoSchema(BaseModel):
    pDif: Optional[float] = Field(None, description="Percentual do Diferimento")
    vDif: Optional[float] = Field(None, description="Valor do Diferimento")


class GrupoDevolucaoTributosSchema(BaseModel):
    vDevTrib: Optional[float] = Field(None, description="Valor do tributo devolvido")


class GrupoReducaoAliquotaSchema(BaseModel):
    pRedAliq: Optional[float] = Field(None, description="Percentual da reducao de aliquota")
    pAliqEfet: Optional[float] = Field(None, description="Aliquota Efetiva que sera aplicada na BC")


class ISSchema(BaseModel):
    CSTIS: Optional[str] = Field(None, description="Codigo da situacao tributaria do Imposto Seletivo")
    cClassTribIS: Optional[str] = Field(None, description="Codigo da situacao tributaria do Imposto Seletivo")
    vBCIS: Optional[float] = Field(None, description="Valor da Base de Calculo do Imposto Seletivo")
    pIS: Optional[float] = Field(None, description="Aliquota do Imposto Seletivo")
    pISEspec: Optional[float] = Field(None, description="Aliquota especifica por unidade de medida apropriada")
    uTrib: Optional[str] = Field(None, description="Unidade de medida tributavel")
    qTrib: Optional[float] = Field(None, description="Quantidade tributavel")
    vIS: Optional[float] = Field(None, description="Valor do Imposto Seletivo")
    memoriaCalculo: Optional[str]= Field(None, description="Memoria de Calculo")


class gIBSUFSchema(BaseModel):
    pIBSUF: Optional[float] = Field(None, description="Aliquota do IBS de competencia das UF")
    gDif: Optional[GrupoDiferimentoSchema] = None
    gDevTrib: Optional[GrupoDevolucaoTributosSchema] = None
    gRed: Optional[GrupoReducaoAliquotaSchema] = None
    vIBSUF: Optional[float] = Field(None, description="Valor do IBS de competencia da UF")
    memoriaCalculo: Optional[str] = Field(None, description="Memoria de Calculo")


class gIBSMunSchema(BaseModel):
    pIBSMun: Optional[float] = Field(None, description="Aliquota do IBS de competencia do Municipio")
    gDif: Optional[GrupoDiferimentoSchema] = None
    gDevTrib: Optional[GrupoDevolucaoTributosSchema] = None
    gRed: Optional[GrupoReducaoAliquotaSchema] = None
    vIBSMun: Optional[float] = Field(None, description="Valor do IBS de competenciao do municpio")
    memoriaCalculo: Optional[str] = Field(None, description="Memoria de Calculo")


class gCBSSchema(BaseModel):
    pCBS: Optional[float] = Field(None)
    gDif: Optional[GrupoDiferimentoSchema] = None
    gDevTrib: Optional[GrupoDevolucaoTributosSchema] = None
    gRed: Optional[GrupoReducaoAliquotaSchema] = None
    vCBS: Optional[float] = Field(None)
    memoriaCalculo: Optional[str] = Field(None)


class gTribRegularSchema(BaseModel):
    CSTReg: Optional[str] = Field(None, description="Codigo da situa tributaria do IBS e CBS")
    cClassTribReg: Optional[str] = Field(None, description="Codigo da classificacao tributaria do IBS e CBS")
    pAliqEfetRegIBSUF: Optional[float] = Field(None, description="Valor da Aliquota do IBS da UF")
    vTribRegIBSUF: Optional[float] = Field(None, description="Valor do tributo IBS da UF")    
    pAliqEfetRegIBSMun: Optional[float] = Field(None, description="Valor da aliquota do IBS do Municipio")
    vTribRegIBSMun: Optional[float] = Field(None, description="Valor do tributo da IBS do Municipio")
    pAliqEfetRegCBS: Optional[float] = Field(None, description="Valor da aliquota da CBS")
    vTribRegCBS: Optional[float] = Field(None, description="Valor do tributo da CBS")


class gTribCompraGovSchema(BaseModel):
    pAliqIBSUF: Optional[float] = Field(None, description="Aliquota do IBS de competencia do Estado")
    vTribIBSUF: Optional[float] = Field(None, description="Valor do Tributo do IBS da UF calculado")
    pAliqIBSMun: Optional[float] = Field(None, description="Aliquota do IBS de competencia do Municipio")
    vTribIBSMun: Optional[float] = Field(None, description="Valor do Tributo do IBS do Municipio calculado")
    pAliqCBS: Optional[float] = Field(None, description="Aliquota da CBS")
    vTribCBS: Optional[float] = Field(None, description="Valor do Tributo da CBS calculado")


class gIBSCBSSchema(BaseModel):
    vBC: Optional[float] = Field(None, description="Base de calculo do IBS e da CBS")
    gIBSUF: Optional[gIBSUFSchema] = None
    gIBSMun: Optional[gIBSMunSchema] = None
    vIBS: Optional[float] = Field(None, description="Valor do IBS")
    gCBS: Optional[gCBSSchema] = None
    gTribRegular: Optional[gTribRegularSchema] = None
    gTribCompraGov: Optional[gTribCompraGovSchema] = None


class gMonoPadraoSchema(BaseModel):
    qBCMono: Optional[float] = Field(None, description="Quantidade tributada na monofasia")
    adRemIBS: Optional[float] = Field(None, description="Aliquota ad rem do IBS")
    adRemCBS: Optional[float] = Field(None, description="Aliquota ad rem da CBS")
    vIBSMono: Optional[float] = Field(None, description="Valor do IBS monofasico")
    vCBSMono: Optional[float] = Field(None, description="Valor da CBS monofasica")


# Grupo de informações da Tributação Monofásica Sujeita à Retenção
class gMonoRetenSchema(BaseModel):
    qBCMonoReten: Optional[float] = Field(None, description="Quantidade tributada sujeita a retencao na monofasia")
    adRemIBSReten: Optional[float] = Field(None, description="Aliquota ad rem do IBS sujeito a retencao")
    vIBSMonoReten: Optional[float] = Field(None, description="Valor do IBS monofasico sujeito a retencao")
    adRemCBSReten: Optional[float] = Field(None, description="Aliquota ad rem da CBS sujeita a retencao")
    vCBSMonoReten: Optional[float] = Field(None, description="Valor da CBS monofasica sujeita a retencao")


# Grupo de informações da Tributação Monofásica Retida Anteriormente
class gMonoRetSchema(BaseModel):
    qBCMonoRet: Optional[float] = Field(None, description="Quantidade tributada retida anteriormente")
    adRemIBSRet: Optional[float] = Field(None, description="Aliquota ad rem do IBS retido anteriormente")
    vIBSMonoRet: Optional[float] = Field(None, description="Valor do IBS retido anteriormente")
    adRemCBSRet: Optional[float] = Field(None, description="Aliquota ad rem da CBS retida anteriormente")
    vCBSMonoRet: Optional[float] = Field(None, description="Valor da CBS retida anteriormente")


# Grupo de informações do Diferimento da Tributação Monofásica
class gMonoDifSchema(BaseModel):
    pDifIBS: Optional[float] = Field(None, description="Percentual do diferimento do imposto monofasico do IBS")
    vIBSMonoDif: Optional[float] = Field(None, description="Valor do IBS monofasico diferido")
    pDifCBS: Optional[float] = Field(None, description="Percentual do diferimento do imposto monofasico da CBS")
    vCBSMonoDif: Optional[float] = Field(None, description="Valor da CBS monofasica diferida")


# Grupo de Informações do IBS e CBS em operações com imposto monofásico
class gIBSCBSMonoSchema(BaseModel):
    gMonoPadrao: Optional[gMonoPadraoSchema] = None
    gMonoReten: Optional[gMonoRetenSchema] = None
    gMonoRet: Optional[gMonoRetSchema] = None
    gMonoDif: Optional[gMonoDifSchema] = None
    vTotIBSMonoItem: Optional[float] = Field(None, description="Total de IBS monofasico")
    vTotCBSMonoItem: Optional[float] = Field(None, description="Total de CBS monofasico")


# Transferências de Crédito
class gTransfCredSchema(BaseModel):
    vIBS: Optional[float] = Field(None, description="Valor do IBS a ser transferido")
    vCBS: Optional[float] = Field(None, description="Valor da CBS a ser transferida")


# Ajuste de competência
class gAjusteCompetSchema(BaseModel):
    competApur: Optional[str] = Field(None, description="Ano e mes referencia do periodo de apuracao (AAAA-MM)")
    vIBS: Optional[float] = Field(None, description="Valor do IBS")
    vCBS: Optional[float] = Field(None, description="Valor da CBS")


# Estorno de crédito
class gEstornoCredSchema(BaseModel):
    vIBSEstCred: Optional[float] = Field(None, description="Valor do IBS a ser estornado")
    vCBSEstCred: Optional[float] = Field(None, description="Valor da CBS a ser estornada")


# Grupo de Informações do Crédito Presumido referente ao IBS
class gIBSCredPresSchema(BaseModel):
    pCredPres: Optional[float] = Field(None, description="Percentual do Credito Presumido")
    vCredPres: Optional[float] = Field(None, description="Valor do Credito Presumido")
    vCredPresCondSus: Optional[float] = Field(None, description="Valor do Credito Presumido em condicao suspensiva")


# Grupo de Informações do Crédito Presumido referente a CBS
class gCBSCredPresSchema(BaseModel):
    pCredPres: Optional[float] = Field(None, description="Percentual do Credito Presumido")
    vCredPres: Optional[float] = Field(None, description="Valor do Credito Presumido")
    vCredPresCondSus: Optional[float] = Field(None, description="Valor do Credito Presumido em condicao suspensiva")


# Informações do crédito presumido de IBS para fornecimentos a partir da ZFM
class gCredPresIBSZFMSchema(BaseModel):
    competApur: Optional[str] = Field(None, description="Ano e mês referência do período de apuração (AAAA-MM)")
    tpCredPresIBSZFM: Optional[int] = Field(None, description="Tipo de classificacao de acordo com o art. 450, § 1º, da LC 214/25 para o calculo do credito presumido na ZFM")
    vCredPresIBSZFM: Optional[float] = Field(None, description="Valor do credito presumido calculado sobre o saldo devedor apurado")


# 
class gCredPresOperSchema(BaseModel):
    vBCCredPres: Optional[float] = Field(None, description="")
    cCredPres: Optional[int] = Field(None, description="")
    gIBSCredPres: Optional[gIBSCredPresSchema] = None
    gCBSCredPres: Optional[gCBSCredPresSchema] = None


class IBSCBSSchema(BaseModel):
    CST: Optional[str] = Field(None, description="Codigo de situacao tributaria do IBS e CBS")
    cClassTrib: Optional[str] = Field(None, description="Codigo de classificacao tributaria do IBS e CBS")
    indDoacao: Optional[int] = Field(None, description="Indica a natureza da operacao de doacao, orientando a apuracao e a geracao de debitos ou estornos conforme o cenario")
    gIBSCBS: Optional[gIBSCBSSchema] = None
    gTransfCred: Optional[gTransfCredSchema] = None
    gAjusteCompet: Optional[gAjusteCompetSchema] = None
    gEstornoCred: Optional[gEstornoCredSchema] = None
    # gCredPresOper: Optional[gCredPresOperSchema] = None
    gCredPresIBSZFM: Optional[gCredPresIBSZFMSchema] = None

# Grupo total da CBS
class gCBSTotalSchema(BaseModel):
    vDif: Optional[float] = Field(None, description='Valor total do diferimento')
    vDevTrib: Optional[float] = Field(None, description="Valor total de devolucoes de tributos")
    vCBS: Optional[float] = Field(None, description="Valor total da CBS")
    vCredPres: Optional[float] = Field(None, description='Valor total do credito presumido')
    vCredPresCondSus: Optional[float] = Field(None, description="Valor total do credito presumido em condicao suspensiva")


class gMonoTotalSchema(BaseModel):
    vIBSMono: Optional[float] = Field(None, description="Total do IBS monofasico")
    vCBSMono: Optional[float] = Field(None, description="Total do CBS monofasico")
    vIBSMonoReten: Optional[float] = Field(None, description="Total da IBS monofasica sujeita a retencao")
    vCBSMonoReten: Optional[float] = Field(None, description="Total da CBS monofasica sujeita a retencao")
    vIBSMonoRet: Optional[float] = Field(None, description="Total da IBS monofasica retido anteriormente")
    vCBSMonoRet: Optional[float] = Field(None, description="Total da CBS monofasica retida anteriormente")



# Classe para calculo do tributo
class TribCalcItemSchema(BaseModel):
    IS: Optional[ISSchema] = None
    IBSCBS: Optional[IBSCBSSchema] = None

class ObjetoSchema(BaseModel):
    nObj: int
    tribCalc: TribCalcItemSchema 

# Classes para os valores totais finais
class ISTotalSchema(BaseModel):
    vIS: Optional[float] = Field(None)


class gIBSTotalSchema(BaseModel):
    vDif: Optional[float] = Field(None)
    vDevTrib: Optional[float] = Field(None)
    vIBSUF: Optional[float] = Field(None)
    vIBSMun: Optional[float] = Field(None)
    vIBS: Optional[float] = Field(None)

class IBSCBSTotalSchema(BaseModel):
    vBCIBSCBS: Optional[float] = Field(None, description="Valor total da BC do IBS e da CBS")
    gIBS: Optional[gIBSTotalSchema] = None
    gCBS: Optional[gCBSTotalSchema] = None
    gMono: Optional[gMonoTotalSchema] = None
    gEstornoCred: Optional[gEstornoCredSchema] = None


class TribCalcTotSchema(BaseModel):
    ISTot: Optional[ISTotalSchema] = None
    IBSCBSTot: Optional[IBSCBSTotalSchema] = None

class TotalSchema(BaseModel):
    tribCalc: Optional[TribCalcTotSchema] = None

# --- Modelo Principal da Resposta ----
class ROCDomainSchema(BaseModel):
    objetos: List[ObjetoSchema]
    total: TotalSchema

























