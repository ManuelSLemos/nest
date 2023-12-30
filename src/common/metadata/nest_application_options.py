from enum import Enum
from pydantic import BaseModel
from typing import ( Any, Dict, List, Optional, Union )

from src.common.metadata.global_prefix_options import GlobalPrefixOptions

# TODO: Create http verbs list 
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
    title: str = 'Nestpy API Documentation'
    version: str = '0.1.0'
    openapi_version: str = "3.1.0"
    summary: Optional[str] = None
    description: Optional[str] = None
    # routes: Sequence[BaseRoute]
    # webhooks: Optional[Sequence[BaseRoute]] = None
    tags: Optional[List[Dict[str, Any]]] = None
    servers: Optional[List[Dict[str, Union[str, Any]]]] = None
    terms_of_service: Optional[str] = None
    contact: Optional[Dict[str, Union[str, Any]]] = None
    license_info: Optional[Dict[str, Union[str, Any]]] = None
    separate_input_output_schemas: bool = True

class NestApplicationOptions(BaseModel):
    debug: bool = False
    prefix: GlobalPrefixOptions = GlobalPrefixOptions()
    cors: CorsOptions = CorsOptions()
    swagger: SwaggerOptions = SwaggerOptions() #TODO: Refactor to docs and DocsOptions

