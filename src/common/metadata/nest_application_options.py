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
class DocsOptions(BaseModel):
    title: str = 'Nestpy API Documentation'
    version: str = '0.1.0'
    openapi_version: str = "3.1.0"
    summary: Optional[str] = None
    description: Optional[str] = None
    servers: Optional[List[Dict[str, Union[str, Any]]]] = None
    terms_of_service: Optional[str] = None
    contact: Optional[Dict[str, Union[str, Any]]] = None
    license_info: Optional[Dict[str, Union[str, Any]]] = None
    separate_input_output_schemas: bool = True

class VersioningOptions(BaseModel):
    type: str
    defaultVersioning: str
    header: str
    key: str

class NestApplicationOptions(BaseModel):
    debug: bool = False
    globalPrefix: bool | GlobalPrefixOptions = False
    versioning: bool | VersioningOptions = False
    cors: CorsOptions = CorsOptions()
    docs: DocsOptions = DocsOptions()



