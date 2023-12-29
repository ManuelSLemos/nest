from src.common.decorators.module_decorator import Module
from app_controller import AppController

@Module(
    controllers=[AppController]
)
class AppModule:
    pass
