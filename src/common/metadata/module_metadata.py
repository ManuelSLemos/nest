from pydantic import BaseModel
from typing import ( Any, List )

class ModuleMetadata(BaseModel):
    imports: List[Any] = []
    controllers: List[Any] = []
    providers: List[Any] = []
    exports: List[Any] = []
