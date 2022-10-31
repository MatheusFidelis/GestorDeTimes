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

            jogador = Jogador(dados["nome"], int(dados["camisa"]), dados["posicao"], int(
                dados["idade"]), contrato)

            self.__jogadores.append(jogador)
            self.__tela.mensagem("cadastro realizada com sucesso")
            break

    def novos_dados(self):
        while True:
            dados = self.__tela.dados_jogador()
            if not self.verificar_dados(dados):
                continue
            for jogador in self.__jogadores:
                if jogador.camisa == int(dados["camisa"]):
                    self.__tela.mensagem_erro("número da camisa existente")
                    continue

            #contrato = Contrato(dados["contrato"]["salario"], dados["contrato"]["multa"]) #objeto contrato

            #jogador = Jogador(dados["nome"], int(dados["idade"]), dados["posicao"], int(
            #    dados["camisa"]), contrato)


            return dados

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

    def dados_jogador(self, jogador): # transforma os dados em dicionario
        dados = {"nome": jogador.nome, "idade": jogador.idade, "posicao": jogador.posicao,
                 "camisa": jogador.camisa, "salario": jogador.contrato.salario, "multa": jogador.contrato.multa}

        return dados

    def seleciona_jogador(self):
        valid = False
        while not valid:
            try:
                camisa = int(self.__tela.seleciona())
            except ValueError:
                self.__tela.mensagem_erro("Por favor digite um valor numérico inteiro")
            else:
                valid = True
        return camisa

    def alterar(self):
        camisa = self.seleciona_jogador()

        i = 0
        encontrado = False
        while i < len(self.__jogadores) and (not encontrado):
            print(self.__jogadores[i].camisa)
            if self.__jogadores[i].camisa == camisa:
                encontrado = True
                posicao = i
            i += 1

        if not encontrado:
            self.__tela.mensagem_erro("Jogador não encontrado")
            return

        dados = self.novos_dados()
        print(dados)
        contrato = Contrato(dados["contrato"]["salario"], dados["contrato"]["multa"])  # objeto contrato

        try:
            jogador = Jogador(dados["nome"], (dados["camisa"]), dados["posicao"], int(dados["idade"]), contrato)

            self.__jogadores.pop(posicao)
            self.__jogadores.append(jogador)
            self.__tela.mensagem("Alteração realizada com sucesso")

            #self.__jogadores[posicao].nome = dados["nome"]
            #self.__jogadores[posicao].idade = dados["idade"]
            #self.__jogadores[posicao].posicao = dados["posicao"]
            #elf.__jogadores[posicao].camisa = dados["camisa"]
            #elf.__jogadores[posicao].contrato.salario = dados['contrato']['salario']
            #self.__jogadores[posicao].contrato.multa = dados['contrato']['multa']
        except:
            print("Erro ao tentar alterar")


        print(self.__jogadores)


    def remover(self): #aqui vai a rescisao
        self.__tela.mensagem("=== REMOVER JOGADOR ===")

        if self.__jogadores == []:
            self.__tela.mensagem_erro("Não há jogadores cadastrados.")
            return

        camisa = int(self.__tela.seleciona())
        i = 0
        encontrado = False
        try:
            while (i < len(self.__jogadores)) and (not encontrado):
                if self.__jogadores[i].camisa == camisa and self.__tela.confirma_exclusao():
                    self.__jogadores.pop(i)
                    encontrado = True
                    self.__tela.mensagem("Jogador removido com sucesso")
                return
                i += 1
        except:
            self.__tela.mensagem_erro("Jogador não existe")

        else:
            self.__tela.mensagem("Jogador removido com sucesso")



    def listar(self):
        if self.__jogadores == []:
            self.__tela.mensagem_erro("Não há jogador para mostrar")
        for jogador in self.__jogadores:
            self.__tela.mostra_jogador(self.dados_jogador(jogador))
