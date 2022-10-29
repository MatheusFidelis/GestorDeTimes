from controladores.controlador_abstrato import ControladorAbstrato
from entidades.class_jogador import Jogador
from telas.tela_elenco import TelaElenco


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
                if opcao in opcoes.keys():
                    opcoes[opcao].inicia()
            except:
                self.__tela.mensagem_erro("Comando Inválido")

    def contrato(self):
        while True:
            dados = self.__tela.dados_jogador()
            if not self.verificar_dados(dados):
                continue
            for jogador in self.__jogadores:
                if jogador.camisa == int(dados["camisa"]):
                    self.__tela.mensagem_erro("número da camisa existente")
                    continue
            jogador = Jogador(dados["nome"], int(dados["idade"]), dados["posicao"], int(
                dados["camisa"]), float(dados["salario"]))
            self.__jogadores.append(jogador)
            self.__tela.mensagem("cadastro realizada com sucesso")
            break

    def verificar_dados(self, dados):
        if dados["nome"].strip() == "":
            self.__tela.mensagem_erro("Nome não pode estar vazio")
            return False
        if not dados["idade"].isnumeric():
            self.__tela.mensagem_erro("Comando invalido")
            return False
        if not dados["posicao"].strip() == "":
            self.__tela.mensagem_erro("Nome não pode estar vazio")
            return False
        if not dados["camisa"].isnumeric():
            self.__tela.mensagem_erro("Comando invalido")
            return False
        if not isinstance(dados["camisa"], float):
            self.__tela.mensagem_erro("Numero Invalido")
            return False
        return True

    def dados_jogador(self, jogador):
        dados = {"nome": jogador.nome, "idade": jogador.idade, "posicao": jogador.posicao,
                 "camisa": jogador.camisa, "salario": jogador.salario}
        return dados

    def seleciona_jogador(self):
        camisa = self.__tela.seleciona()
        for jogador in self.__jogadores:
            if jogador.camisa == int(camisa):
                return jogador

    def alterar(self):
        jogador = self.seleciona_jogadores()
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

    '''def remover(self): aqui vai a rescisao'''

    def listar(self):
        for jogador in self.__jogadores:
            self.__tela.mostra_jogador(self.dados_jogador(jogador))
