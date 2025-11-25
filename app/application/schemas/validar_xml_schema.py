from pydantic import BaseModel, Field
from typing import Optional, List
from app.application.enums.tipo_documento_enum import TipoDocumentoEnum


class ValidateXMLSchema(BaseModel):
    def __init__(self, type: TipoDocumentoEnum, subtype):
        pass