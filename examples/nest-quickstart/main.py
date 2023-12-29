from packages.core.nest_application import NestAplication
from app_module import AppModule

def bootstrap():
    app = NestAplication( AppModule )

    app.enableSwaggerUI('/docs')
    app.enableRedoc('/redoc')

    app.enableCors()

    @app.app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.app.post("/")
    def create_root():
        return {"Hello": "World"}

    @app.app.put("/")
    def update_root():
        return {"Hello": "World"}

    @app.app.delete("/")
    def delete_root():
        return {"Hello": "World"}

    app.listen( host='0.0.0.0', port=3000 )

if __name__ == "__main__":
    bootstrap()