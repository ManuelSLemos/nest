from src.common.decorators.module_decorator import Module
from users.user_controller import UserController

@Module(
    controllers=[UserController]
)
class UserModule:
    pass
