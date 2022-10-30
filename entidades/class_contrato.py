class Contrato():
    def __init__(self, salario: float, multa: float):
        self._salario = salario
        self._multa = multa

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario (self, salario: float):
        self._salario = salario

    @property
    def multa(self):
        return self._multa

    @multa.setter
    def multa(self, multa: float):
        self._multa = multa
