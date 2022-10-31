class Time:
    def __init__(self, nome: str, orcamento: float):
        self.__nome = nome
        self.__orcamento = orcamento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def orcamento(self):
        return self.__orcamento

    @orcamento.setter
    def orcamento(self, orcamento):
        self.__orcamento = orcamento
