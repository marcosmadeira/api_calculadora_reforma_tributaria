# app/domain/value_objects/resultado.py
from dataclasses import dataclass

@dataclass(frozen=True)
class Resultado:
    valor_total_faturado: float
    valor_ibs: float
    valor_cbs: float
    valor_total_impostos: float