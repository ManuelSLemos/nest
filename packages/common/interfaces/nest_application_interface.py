from abc import ( ABC, abstractmethod )

class INestAplication(ABC):

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
