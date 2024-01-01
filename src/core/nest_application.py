from typing import ( Any, List )

from fastapi import FastAPI, APIRouter

from src.common.enums import VersioningType
from src.common.decorators.module_decorator import Module
from src.common.interfaces import INestAplication
from src.common.metadata.nest_application_options import ( NestApplicationOptions, GlobalPrefixOptions, VersioningOptions )

import uvicorn

class NestAplication(INestAplication):

    def __init__(self, 
        appModule: Module, 
        config: NestApplicationOptions = NestApplicationOptions()
    ):
        self.nest = self._createServer()
        self.appModule = appModule()
        self.config = self._setConfig(config)


    def _createServer(self, docs_url=None, redoc_url=None) -> FastAPI: 
        return FastAPI(docs_url=docs_url, redoc=redoc_url)

    def _setConfig(self, value: NestApplicationOptions) -> NestApplicationOptions:
        if type(value.globalPrefix == bool):
            value.globalPrefix = GlobalPrefixOptions(
                prefix= '/api' if value.globalPrefix else ''
            )

        if type(value.versioning == bool):
            value.versioning = VersioningOptions(
                type=VersioningType.URI,
                defaultVersioning='1'
            )
        
        return value

    def _setup(self) -> None:
        self._setupVersioning()
        self._setupModule()

    def _setupModule(self) -> None:
        controllers = self.appModule.controllers

        for module in self.appModule.imports:
            controllers.extend(module().controllers)

        self._setupController(controllers)

    def _setupController(self, controllers: List[Any]) -> None:
        globalPrefix = self.config.globalPrefix.prefix
        for controller in controllers:
            router = APIRouter(
                prefix=f'{globalPrefix}{controller().prefix}',
                tags=controller().tags)
            
            for route in controller().routes:
                router.add_api_route(
                    route.prefix,
                    route.attr,
                    methods=[route.method])

            self.nest.include_router(router)
    
    def _setupVersioning(self) -> None:
        options = self.config.versioning

        if options.type == VersioningType.URI:
            pass

        if options.type == VersioningType.HEADER:
            pass

        if options.type == VersioningType.MEDIA_TYPE:
            pass

        if options.type == VersioningType.CUSTOM:
            pass

    def enableVersioning(self, type: VersioningType, defaultVersioning: str) -> None:
        pass

    def listen(self, host: str = '0.0.0.0', port: int = 8080) -> None:
        self._setup()

        uvicorn.run(self.nest, host=host, port=port)

    def setGlobalPrefix(self, prefix: str, exclude: List[str] = []) -> None:
        self.config.globalPrefix = GlobalPrefixOptions(
            prefix=prefix,
            exclude=exclude
        )
    