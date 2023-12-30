from typing import ( List, Dict, Any )

from fastapi import FastAPI, APIRouter

from src.common.metadata.nest_application_options import ( 
    NestApplicationOptions, 
    CorsOptions, 
    DocsOptions, 
    GlobalPrefixOptions 
)

class NestAplication():

    def __init__(self, 
        module: Any = None, 
        config: NestApplicationOptions = NestApplicationOptions()
    ):
        self.nest = self._createServer()
        self.module = module
        self.config = config

    def _createServer(self) -> FastAPI: 
        return FastAPI(docs_url=None, redoc_url=None)

    def _setup(self) -> None: pass
    
    def listen(self, host: str = '0.0.0.0', port: int = 8080) -> None:
        self._setup()

        uvicorn.run(self.nest, host=host, port=port)

    