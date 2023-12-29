from packages.core.common.decorators.module_decorator import Module
from packages.core.common.decorators.controller_decorator import Controller
from packages.core.common.decorators.http_verbs_decorators import ( 
    Delete, 
    Get, 
    Post, 
    Put 
)


@Controller('/app')
class AppController:
    @Get('/')
    def findAll():
        pass

    @Get('/{id}')
    def findById(id: str):
        pass

    @Post('/')
    def create():
        pass

    @Put('/{id}')
    def update(id: str):
        pass

    @Delete('/{id}')
    def delete(id: str):
        pass


@Module(
    controllers=[AppController]
)
class AppModule:
    pass


appModule = AppModule()
print(type(appModule))
appModule.controllers[0]()

# cls = appModule.controllers[0]()

# for attr_name in dir(cls):
#     attr = getattr(cls, attr_name)
#     if callable(attr) and hasattr(attr, "is_route"):
#         prefix, method = getattr(attr, "route_info")
#         print(prefix, method)


# appController = AppController()
# print(type(appController))
# print(appController.path)
