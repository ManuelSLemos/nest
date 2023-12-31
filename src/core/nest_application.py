from typing import ( Any, List )

from fastapi import FastAPI, APIRouter

from src.common.metadata.nest_application_options import ( NestApplicationOptions, GlobalPrefixOptions )
from src.common.decorators.module_decorator import Module

import uvicorn

class NestAplication():

    def __init__(self, 
        appModule: Module, 
        config: NestApplicationOptions = NestApplicationOptions()
    ):
        self.nest = self._createServer()
        self.appModule = appModule()
        self.config = config


    def _createServer(self) -> FastAPI: 
        return FastAPI()

    def _setup(self) -> None:
        self._setupModule()

    def _setupModule(self) -> None:
        controllers = self.appModule.controllers

        for module in self.appModule.imports:
            controllers.extend(module().controllers)

        self._setupController(controllers)

    def _setupController(self, controllers: List[Any]) -> None:
        for controller in controllers:
            router = controller().router
            
            for route in controller().routes:
                router.add_api_route(
                    route.prefix,
                    route.attr,
                    methods=[route.method])

            self.nest.include_router(router)
    
    def listen(self, host: str = '0.0.0.0', port: int = 8080) -> None:
        self._setup()

        uvicorn.run(self.nest, host=host, port=port)

    def setGlobalPrefix(self, prefix: str, options: GlobalPrefixOptions = None) -> None:
        if options is not None:
            self.options.globalPrefix = options

        self.options.globalPrefix = GlobalPrefixOptions(prefix=prefix)
    