from src.common.decorators.controller_decorator import Controller
from src.common.decorators.http_verbs_decorators import ( 
    Delete, 
    Get, 
    Post, 
    Put 
)

@Controller('/users')
class UserController:
    
    @Get('/')
    async def findAll() -> str:
        return {"Hello": "World"}

    @Get('/{id}')
    async def findById(id: str) -> str:
        return {"Hello": id}

    @Post('/')
    async def create() -> str:
        return {"Hello": "World"}

    @Put('/{id}')
    async def update(id: str) -> str:
        return {"Hello": id}

    @Delete('/{id}')
    async def delete(id: str) -> str:
        return {"Hello": id}

