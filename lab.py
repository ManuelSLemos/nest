from packages.core.common.decorators.module_decorator import Module
from packages.core.common.decorators.controller_decorator import Controller

@Controller('/app')
class AppController:
    pass


@Module(
    controllers=[AppController]
)
class AppModule:
    pass


appModule = AppModule()
print(type(appModule))
print(appModule.controllers[0]().path)


# appController = AppController()
# print(type(appController))
# print(appController.path)
