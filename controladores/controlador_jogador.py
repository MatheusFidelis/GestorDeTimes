from controladores.controlador_abstrato import ControladorAbstrato
from entidades.class_jogador import Jogador
from telas.tela_elenco import TelaElenco
from entidades.class_contrato import Contrato

class ControladorJogador(ControladorAbstrato):

    def __init__(self):
        self.__jogadores = []
        self.__tela = TelaElenco()

    def inicia(self):
        opcoes = {"1": self.contrato, "2": self.alterar,
                  "3": self.listar, "4": self.remover}
        while True:
            opcao = self.__tela.opcoes()
            if opcao == "0":
                break
            try:
                opcoes[opcao]()
            except:
                self.__tela.mensagem_erro("Comando Inválido ( sessão elenco )")

    def contrato(self):
        while True:
            dados = self.__tela.dados_jogador()
            if not self.verificar_dados(dados):
                continue
            for jogador in self.__jogadores:
                if jogador.camisa == int(dados["camisa"]):
                    self.__tela.mensagem_erro("número da camisa existente")
                    continue

            contrato = Contrato(dados["contrato"]["salario"], dados["contrato"]["multa"]) #objeto contrato

            jogador = Jogador(dados["nome"], int(dados["idade"]), dados["posicao"], int(
                dados["camisa"]), contrato)

            self.__jogadores.append(jogador)
            self.__tela.mensagem("cadastro realizada com sucesso")
            break

    def verificar_dados(self, dados):


        if len(dados["nome"]) == 0:
            self.__tela.mensagem_erro("Nome não pode estar vazio")
            return False
        if not dados["idade"].isnumeric():
            self.__tela.mensagem_erro("Valor inválido para idade")
            return False
        if len(dados["posicao"]) == 0:
            self.__tela.mensagem_erro("Posicao não pode estar vazio")
            return False
        if not dados["camisa"].isnumeric():
            self.__tela.mensagem_erro("Camisa invalido")
            return False


        return True

    def dados_jogador(self, jogador):
        dados = {"nome": jogador.nome, "idade": jogador.idade, "posicao": jogador.posicao,
                 "camisa": jogador.camisa}
        print('dados')
        print(jogador.contrato.salario)

        print(jogador.contrato.multa)
        return dados

    def seleciona_jogador(self):
        camisa = self.__tela.seleciona()
        for jogador in self.__jogadores:
            if jogador.camisa == int(camisa):
                return jogador
        return False


    def alterar(self):
        jogador = self.seleciona_jogador()
        if isinstance(jogador, Jogador):
            self.__tela.mostra_jogador(self.dados_jogador(jogador))
            while True:
                dados = self.__tela.dados_alterar()
                dados["camisa"] = Jogador.camisa
                if not self.verificar_dados(dados):
                    continue
                jogador.nome = dados["nome"]
                jogador.idade = dados["idade"]
                jogador.posicao = dados["posicao"]
                jogador.camisa = dados["camisa"]
                self.__tela.mensagem("Alteração realizada com sucesso")
                break
        else:
            self.__tela.mensagem_erro("Jogador não encontrado")

    def remover(self): #aqui vai a rescisao
        self.__tela.mensagem("=== REMOVER JOGADOR ===")
        camisa = self.__tela.seleciona()
        i = 0
        encontrado = False
        try:
            while i < len(self.__jogadores) and not encontrado:
                if self.__jogadores[i].camisa == camisa:
                    self.__jogadores.pop(i)
                    encontrado = True
                    self.__tela.mensagem("Jogador removido com sucesso")
                return
                i += 1
        except:
            self.__tela.mensagem_erro("Jogador não encontrado")



    def listar(self):
        if self.__jogadores == []:
            self.__tela.mensagem_erro("Não há jogador para mostrar")
        for jogador in self.__jogadores:
            self.__tela.mostra_jogador(self.dados_jogador(jogador))
