from typing import ( List, Dict, Any )

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

import uvicorn

from src.common.interfaces.nest_application_interface import INestAplication
from src.common.metadata.nest_application_options import ( NestApplicationOptions, CorsOptions, SwaggerOptions )

class NestAplication(INestAplication):
    
    def __init__(
            self,
            appModule: Any,
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

    def enableSwaggerUI(self, url: str = '/docs', options: SwaggerOptions = None) -> None:
        self.__enableOpenapi(options)
        self.app.docs_url = url

    def enableRedoc(self, url: str = '/redoc', options: SwaggerOptions = None) -> None:
        self.__enableOpenapi(options)
        self.app.redoc_url = url
    
    def listen(self, host: str = '0.0.0.0', port: int = 8080) -> None:
        self.app.setup()

        uvicorn.run( self.app, host=host, port=port )

    def _register_modules(self):
        for controller in self.appModule().controllers:
            router = controller().router
            self.app.include_router(router)

        for module in self.appModule().imports:
            for controller in module().controllers:
                router = controller().router
                self.app.include_router(router)

    def __openapi(self):
        if self.app.openapi_schema:
            return self.app.openapi_schema

        openapi_schema = get_openapi(
            title=self.options.swagger.title,
            version=self.options.swagger.version,
            openapi_version=self.options.swagger.openapi_version,
            summary=self.options.swagger.summary,
            description=self.options.swagger.description,
            terms_of_service=self.options.swagger.terms_of_service,
            contact=self.options.swagger.contact,
            license_info=self.options.swagger.license_info,
            routes=self.app.routes,
            webhooks=self.app.webhooks.routes,
            tags=self.options.swagger.tags,
            servers=self.options.swagger.servers,
            separate_input_output_schemas=self.options.swagger.separate_input_output_schemas,
        )

        self.app.openapi_schema = openapi_schema

        return self.app.openapi_schema

    def __enableOpenapi(self, options: SwaggerOptions = None):
        if options is not None:
            self.options.swagger = options

        self.app.openapi = self.__openapi




    