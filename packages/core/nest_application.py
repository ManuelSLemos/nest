from typing import List
from fastapi import FastAPI, APIRouter

import uvicorn

from packages.common.interfaces.nest_application_interface import INestAplication

class NestAplication(INestAplication):
    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    def __init__(self):
        pass
    
    def listen(self, host: str = '0.0.0.0', port: int = 8080) -> None:
        uvicorn.run( self.app, host=host, port=port )