from src.core.nest_application import NestAplication
from app_module import AppModule

def bootstrap():
    app = NestAplication( AppModule )

    app.setGlobalPrefix( '/api' )

    app.enableSwaggerUI('/docs')
    app.enableRedoc('/redoc')

    app.enableCors()

    app.listen( host='0.0.0.0', port=3000 )

if __name__ == "__main__":
    bootstrap()