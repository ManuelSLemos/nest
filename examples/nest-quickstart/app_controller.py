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
    async def findAll():
        return {"Hello": "World"}

    @Get('/{id}')
    async def findById(id: str):
        return {"Hello": id}

    @Post('/')
    async def create():
        return {"Hello": "World"}

    @Put('/{id}')
    async def update(id: str):
        return {"Hello": id}

    @Delete('/{id}')
    async def delete(id: str):
        return {"Hello": id}

