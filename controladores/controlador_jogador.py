from controladores.controlador_abstrato import ControladorAbstrato
from entidades.class_jogador import Jogador
from telas.tela_elenco import TelaElenco
from entidades.class_contrato import Contrato

class ControladorJogador(ControladorAbstrato):

    def __init__(self):
        self.__jogadores = []
        self.__tela = TelaElenco()
        self.__historico = []
        self.__despesa = 0
        #self.__orcamento = time.orcamento()

    @property
    def despesa(self):
        return self.__despesa

    @despesa.setter
    def despesa(self, despesa):
        self.__despesa = despesa

    @property
    def jogadores(self):
        return self.__jogadores

    @jogadores.setter
    def jogadores(self, jogador):
        self.__jogadores.append(jogador)

    def inicia(self):
        opcoes = {"1": self.contrato, "2": self.alterar,
                  "3": self.listar, "4": self.remover, "5": self.historico_jogadores,
                  "6": self.checa_despesa}
        while True:
            opcao = self.__tela.opcoes()
            if opcao == "0":
                break
            try:
                opcoes[opcao]()
            except:
                self.__tela.mensagem_erro("Comando Inválido ( sessão elenco )")

    def atualiza_historico(self, dados):
        self.__historico.append({'nome': dados['nome'], 'camisa': dados['camisa'], 'acao': dados['acao']})

    def contrato(self):
        while True:
            dados = self.__tela.dados_jogador()
            if not self.verificar_dados(dados):
                continue
            for jogador in self.__jogadores:
                if jogador.camisa == int(dados["camisa"]):
                    self.__tela.mensagem_erro("número da camisa existente")
                    break

            contrato = Contrato(dados["contrato"]["salario"], dados["contrato"]["multa"]) #objeto contrato

            jogador = Jogador(dados["nome"], int(dados["camisa"]), dados["posicao"], int(
                dados["idade"]), contrato)

            self.__despesa += dados['contrato']['salario']
            self.atualiza_historico({'nome': dados['nome'], 'camisa': dados['camisa'], 'acao': 'adiciona'})
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
        if self.__jogadores == []:
            self.__tela.mensagem_erro("Não há jogadores cadastrados")
            return
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

        i = 0

        while i < len(self.__jogadores): #verifica se camisa já existe
            if self.__jogadores[i] == camisa and (i != posicao):
                self.__tela.mensagem_erro("Camisa já existe")
                return

            i += 1
        dados = self.novos_dados()
        contrato = Contrato(dados["contrato"]["salario"], dados["contrato"]["multa"])  # objeto contrato

        try:
            jogador = Jogador(dados["nome"], (dados["camisa"]), dados["posicao"], int(dados["idade"]), contrato)

            dados_historico = {'nome': dados['nome'], 'camisa': dados['camisa'], 'acao': 'alteracao'}
            self.atualiza_historico(dados_historico)
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
                if self.__jogadores[i].camisa == camisa and self.__tela.confirma_exclusao() == '0':
                    jogador = self.__jogadores.pop(i)
                    self.__tela.mensagem("Jogador removido com sucesso")

                    encontrado = True
                i += 1

            dados_historico = {
                'nome': jogador.nome,
                'camisa': jogador.camisa,
                'acao': 'removido'
            }

            self.atualiza_historico(dados_historico)
            dados = self.dados_jogador(jogador)
            print(dados)
            self.__despesa -= (dados['salario'])

        except:
            self.__tela.mensagem_erro("Jogador não existe")

        else:
            self.__tela.mensagem("Jogador removido com sucesso")


    def listar(self):
        if self.__jogadores == []:
            self.__tela.mensagem_erro("Não há jogador para mostrar")
            return
        for jogador in self.__jogadores:
            self.__tela.mostra_jogador(self.dados_jogador(jogador))

    def historico_jogadores(self):
        self.__tela.mensagem("Histórico de jogadores")

        if self.__historico == []:
            self.__tela.mensagem_erro("Nenhuma movimentação.")
            return

        i = 1
        for dado in self.__historico:
            self.__tela.mensagem_historico(f"\nNome: {dado['nome']} \nCamisa: {dado['camisa']}\nAcao: {dado['acao']} \n {'_' * 20}", i)
            i += 1

    def checa_despesa(self):
        self.__tela.mensagem("Despesas")
        self.__tela.mensagem(f"Total despesa: R${self.__despesa}")

    def checa_orcamento(self):
        self.__tela.mensagem("Orcamento")
