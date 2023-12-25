from typing import List
from fastapi import FastAPI, APIRouter

import uvicorn

class NestAplication():
    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    def __init__(self):
        pass
    
    def listen(self, port: int = 8080) -> None:
        uvicorn.run(
            self.app,
            host="0.0.0.0",
            port=port,
        )