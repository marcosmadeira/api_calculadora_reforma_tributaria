from enum import Enum

class SubtipoDocumentoEnum(str, Enum):
    """
    Enum para os subtipos de documentos suportados pela API de validação
    """
    grupo = "grupo"
    nota = "nota"