from entidades.class_time import Time
from telas.tela_time import TelaTime

class ControladorTime():
    def __init__(self):
        self.__tela = TelaTime()

        dados_time = self.__tela.dados_time()
        self.__time = Time(dados_time['nome'], float(dados_time['orcamento']))

#    def cadastrar_time(self):

    def time_orcamento(self):
        return self.__time.orcamento

    # TODO: adicionar orcamento
    # def adicionar_orcamento(self):