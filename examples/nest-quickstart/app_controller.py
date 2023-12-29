from src.common.decorators.controller_decorator import Controller
from src.common.decorators.http_verbs_decorators import ( 
    Delete, 
    Get, 
    Post, 
    Put 
)

@Controller('/')
class AppController:
    
    @Get('/')
    async def findAll():
        return {"Hello": "World"}
