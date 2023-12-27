from typing import List
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from packages.common.interfaces.nest_application_interface import INestAplication
from packages.core.nest_application_options import ( NestApplicationOptions, CorsOptions, SwaggerOptions )

class NestAplication(INestAplication):
    
    def __init__(
            self, 
            options: NestApplicationOptions = NestApplicationOptions()
        ):
            self.app = FastAPI( debug = options.debug, docs_url = None, redoc_url = None )

            @self.app.get("/")
            def read_root():
                return {"Hello": "World"}

    def enableCors(self, options: CorsOptions = None):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def enableSwagger(self, options: SwaggerOptions = None):
        pass
    
    def listen(self, host: str = '0.0.0.0', port: int = 8080) -> None:
        uvicorn.run( self.app, host=host, port=port )

    