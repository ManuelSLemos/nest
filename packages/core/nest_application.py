from typing import List
from fastapi import FastAPI, APIRouter

import uvicorn

from packages.common.interfaces.nest_application_interface import INestAplication
from packages.core.nest_application_options import NestApplicationOptions

class NestAplication(INestAplication):
    
    def __init__(
            self, 
            options: NestApplicationOptions = NestApplicationOptions()
        ):
            self.app = FastAPI( debug = options.debug )

            @self.app.get("/")
            def read_root():
                return {"Hello": "World"}
    
    def listen(self, host: str = '0.0.0.0', port: int = 8080) -> None:
        uvicorn.run( self.app, host=host, port=port )

    