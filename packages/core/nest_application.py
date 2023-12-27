from typing import List, Dict, Any
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from packages.core.common.interfaces.nest_application_interface import INestAplication
from packages.core.common.metamodels.nest_application_options import ( NestApplicationOptions, CorsOptions, SwaggerOptions )

class NestAplication(INestAplication):
    
    def __init__(
            self, 
            options: NestApplicationOptions = NestApplicationOptions()
        ):
            self.app = FastAPI( debug = options.debug, docs_url = None, redoc_url = None )
            self.options = options

    def enableCors(self, options: CorsOptions = None):
        options = self.options.cors if options is None else options

        self.app.add_middleware(
            CORSMiddleware,
            allow_credentials=options.credentials,
            expose_headers=options.exposedHeaders,
            allow_headers=options.allowedHeaders,
            allow_origins=options.origins,
            allow_methods=options.methods,
            max_age=options.maxAge
        )

    def enableSwagger(self, options: SwaggerOptions = None):
        pass
    
    def listen(self, host: str = '0.0.0.0', port: int = 8080) -> None:
        uvicorn.run( self.app, host=host, port=port )

    