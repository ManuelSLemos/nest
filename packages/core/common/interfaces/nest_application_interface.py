from abc import ( ABC, abstractmethod )

from packages.core.common.metamodels.nest_application_options import ( NestApplicationOptions, CorsOptions, SwaggerOptions )

class INestAplication(ABC):

    @abstractmethod
    def enableCors(self, options: CorsOptions = None):
        pass

    @abstractmethod
    def enableSwaggerUI(self, options: SwaggerOptions = None):
        pass

    @abstractmethod
    def enableRedoc(self, options: SwaggerOptions = None):
        pass

    @abstractmethod
    def listen(self, host: str = '0.0.0.0', port: int = 8080) -> None:
        """Starts the application.

        Parameters
        ----------

        port : int, optional
        host : str, optional
    
        Returns
        -------

        """    
        pass
    
    @abstractmethod
    def _register_modules(self):
        """
        Registers the modules from the app modules.
        """
        pass

