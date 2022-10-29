from abc import abstractmethod, ABC


class ControladorAbstrato(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def inicia(self):
        pass
