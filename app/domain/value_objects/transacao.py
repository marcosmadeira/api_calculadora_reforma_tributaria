# app/domain/value_objects/transacao.py
from dataclasses import dataclass

@dataclass(frozen=True)
class Transacao:
    valor: float
    categoria: str