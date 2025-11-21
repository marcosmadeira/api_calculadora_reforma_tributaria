from enum import Enum

class TipoDocumentoEnum(str, Enum):
    """Enum para os tipos de documentos suportados pela API de geração de XML."""
    nfe = "nfe"
    nfce = "nfce"
    nfse = "nfse"
    cte = "cte"
    cte_simplificado = "cte-simplificado"
    bpe = "bpe"
    bpe_tm = "bpe-tm"
    nf3e = "nf3e"