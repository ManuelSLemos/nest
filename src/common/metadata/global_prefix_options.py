from pydantic import BaseModel
from typing import ( List )

class Route(BaseModel):
    prefix: str
    method: str
    tag: str

class GlobalPrefixOptions(BaseModel):
    prefix: str = '/api'
    exclude: List[Route] = []
