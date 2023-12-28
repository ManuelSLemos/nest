from packages.core.common.decorators.module_decorator import Module

@Module(
    controllers=['Hola']
)
class AppModule:
    pass


appModule = AppModule()
print(type(appModule))
print(appModule.controllers)