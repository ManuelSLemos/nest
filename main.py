from packages.core.nest_application import NestAplication
from packages.core.common.metamodels.nest_application_options import ( NestApplicationOptions, CorsOptions, SwaggerOptions )

def bootstrap():
    app = NestAplication(options=NestApplicationOptions(cors=CorsOptions(credentials=True)))

    app.enableSwaggerUI('/docs')
    app.enableRedoc('/redoc')

    app.enableCors(options=CorsOptions(credentials=False))

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