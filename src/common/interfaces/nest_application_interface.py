from abc import ( ABC, abstractmethod )

from src.common.metadata.nest_application_options import ( CorsOptions, DocsOptions )

class INestAplication(ABC):

    @abstractmethod
    def enableCors(self, options: CorsOptions = None):
        pass

    @abstractmethod
    def enableSwaggerUI(self, options: DocsOptions = None):
        pass

    @abstractmethod
    def enableRedoc(self, options: DocsOptions = None):
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
    def setGlobalPrefix(self, prefix: str, options = None) -> None:
        pass

    @abstractmethod
    def _register_modules(self):
        """
        Registers the modules from the app modules.
        """
        pass

