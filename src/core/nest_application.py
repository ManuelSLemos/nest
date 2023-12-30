from typing import ( List, Dict, Any )

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

import uvicorn

from src.common.interfaces.nest_application_interface import INestAplication
from src.common.metadata.nest_application_options import ( 
    NestApplicationOptions, 
    CorsOptions, 
    DocsOptions, 
    GlobalPrefixOptions 
)

class NestAplication(INestAplication):
    
    def __init__(
            self,
            appModule: Any, # TODO: Change for type
            options: NestApplicationOptions = NestApplicationOptions()
        ):
            self.appModule = appModule
            self.options = options

            self.app = FastAPI( debug = options.debug, docs_url=None, redoc_url=None )
            self._register_modules()


    def enableCors(self, options: CorsOptions = None) -> None:
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

    def enableSwaggerUI(self, url: str = '/docs', options: DocsOptions = None) -> None:
        self.__enableOpenapi(options)
        self.app.docs_url = url

    def enableRedoc(self, url: str = '/redoc', options: DocsOptions = None) -> None:
        self.__enableOpenapi(options)
        self.app.redoc_url = url
    
    def listen(self, host: str = '0.0.0.0', port: int = 8080) -> None:
        self.setup()

        uvicorn.run( self.app, host=host, port=port )

    def setup(self):
        if self.options.globalPrefix: self._enableGlobalPrefix()

        self.app.setup()

    def setGlobalPrefix(self, prefix: str, options: GlobalPrefixOptions = None) -> None:
        if options is not None:
            self.options.globalPrefix = options

        self.options.globalPrefix = GlobalPrefixOptions(prefix=prefix)

    # TODO: Refactor controllers loader
    def _register_modules(self):
        for controller in self.appModule().controllers:
            router = controller().router
            self.app.include_router(router)

        for module in self.appModule().imports:
            for controller in module().controllers:
                router = controller().router
                self.app.include_router(router)

    def _enableGlobalPrefix(self):
        typeOption = type(self.options.globalPrefix)
        if typeOption == bool: self.options.globalPrefix = GlobalPrefixOptions()

        routes = self.app
        app = FastAPI( debug = self.options.debug, docs_url=None, redoc_url=None )
        app.mount(self.options.globalPrefix.prefix, routes)
        self.app = app
    
    def __openapi(self):
        if self.app.openapi_schema:
            return self.app.openapi_schema

        openapi_schema = get_openapi(
            title=self.options.docs.title,
            version=self.options.docs.version,
            openapi_version=self.options.docs.openapi_version,
            summary=self.options.docs.summary,
            description=self.options.docs.description,
            terms_of_service=self.options.docs.terms_of_service,
            contact=self.options.docs.contact,
            license_info=self.options.docs.license_info,
            servers=self.options.docs.servers,
            separate_input_output_schemas=self.options.docs.separate_input_output_schemas,
            routes=self.app.routes,
            webhooks=self.app.webhooks.routes,
        )

        self.app.openapi_schema = openapi_schema

        return self.app.openapi_schema

    def __enableOpenapi(self, options: DocsOptions = None):
        if options is not None:
            self.options.docs = options

        self.app.openapi = self.__openapi




    