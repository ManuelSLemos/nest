from abc import ( ABC, abstractmethod )
from typing import List

from src.common.metadata.nest_application_options import ( 
    CorsOptions, 
    DocsOptions, 
    GlobalPrefixOptions 
)

from src.common.enums import VersioningType 

class INestAplication(ABC):

    @abstractmethod
    def enableVersioning(self, type: VersioningType, defaultVersioning: str) -> None:
        pass

    @abstractmethod
    def listen(self, host: str = '0.0.0.0', port: int = 8080) -> None:    
        pass
    
    @abstractmethod
    def setGlobalPrefix(self, prefix: str, exclude: List[str] = []) -> None:
        pass