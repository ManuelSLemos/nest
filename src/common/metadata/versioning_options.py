from pydantic import BaseModel

from src.common.enums import VersioningType

class VersioningOptions(BaseModel):
    type: VersioningType
    defaultVersioning: str
    header: str
    key: str
