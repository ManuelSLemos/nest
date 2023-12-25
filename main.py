from packages.core.nest_application import NestAplication

def bootstrap():
    app = NestAplication()

    app.listen(3000)

if __name__ == "__main__":
    bootstrap()