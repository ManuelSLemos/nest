from enum import Enum
from pydantic import BaseModel
from typing import ( Any, Dict, List, Optional, Union )

class CorsOptions(BaseModel):
    origins: List[str] = ['*']
    methods: List[str] = ['*']
    allowedHeaders: List[str] = ['*']
    exposedHeaders: List[str] = ['*']
    credentials: bool = False
    maxAge: int = 3600
    # preflightContinue: Optional[bool] = None
    # optionsSuccessStatus: Optional[int] = None

class SwaggerOptions(BaseModel):
    contact: Optional[Dict[str, Union[str, Any]]] = None
    docs_url: str 
    description: Optional[str] = None
    license_info: Optional[Dict[str, Union[str, Any]]] = None
    openapi_url: str
    openapi_version: str
    separate_input_output_schemas: bool = True
    servers: Optional[Dict[str, Any]] = None
    summary: Optional[str] = None
    redoc_url: str
    routes: Any
    tags: Optional[Dict[str, Union[str, Any]]] = None
    terms_of_service: Optional[str] = None
    title: str
    version: str
    webhooks: Any

class NestApplicationOptions(BaseModel):
    debug: bool = False
    cors: CorsOptions = CorsOptions()
    swagger: SwaggerOptions = {}

