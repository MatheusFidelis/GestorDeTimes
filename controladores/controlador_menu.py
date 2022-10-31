from controladores.controlador_jogador import ControladorJogador
from controladores.controlador_orcamento import ControladorOrcamento
from controladores.controlador_abstrato import ControladorAbstrato
from controladores.controlador_time import ControladorTime
from telas.tela_menu import TelaMenu


class ControladorMenu (ControladorAbstrato):

    def __init__(self):
        self.__controlador_jogador = ControladorJogador()
        self.__controlador_orcamento = ControladorOrcamento()
        self.__controlador_time = ControladorTime()
        self.__tela = TelaMenu()

    def inicia(self):
        opcoes = {1: self.__controlador_jogador,
                  2: self.__controlador_orcamento}
        while True:
            opcao = self.__tela.opcoes()
            if opcao == "0":
                break
            self.__controlador_jogador.inicia()
            try:

                opcoes[int(opcao)].inicia()
                print("try OOK")
            except:
                self.__tela.mensagem_erro("Comando Inválido. ( menu principal )")

    @property
    def controlador_orcamento(self):
        return self.__controlador_orcamento

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador
