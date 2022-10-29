class Contrato:
    
    def __init__(self, multa:float):
        self.__multa = multa
        
    @property
    def multa(self):
        return self.__multa
    
    @multa.setter
    def multa(self, multa: float):
        self.__multa = multa