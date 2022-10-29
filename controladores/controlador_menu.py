from controladores.controlador_jogador import ControladorJogador
'''from controladores.controlador_orcamento import ControladorOrcamento''' '''coloque o controlador aqui caso o nome seja diferente'''
from controladores.controlador_abstrato import ControladorAbstrato
from telas.tela_menu import TelaMenu

class ControladorMenu (ControladorAbstrato):
        
    def __init__(self):
        self.__controlador_jogador = ControladorJogador()
        '''self.__controlador_orcamento= ControladorOrcamento()'''
        self.__tela = TelaMenu()
        
    def inicia(self): 
       opcoes = {"1": self.__controlador_jogador,"2": self.__controlador_orcamento}
       while True:
            opcao = self.__tela.opcoes()
            if opcao == "0":
                break
            try:
                if opcao in opcoes.keys():
                    opcoes[opcao].inicia()
            except:
                self.__tela.mensagem_erro("Comando Inválido")
    @property
    def controlador_conta(self):
        return self.__controlador_orcamento
    
    @property
    def controlador_cliente(self):
        return self.__controlador_jogador