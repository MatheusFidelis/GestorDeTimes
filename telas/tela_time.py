from telas.tela_abstrata import TelaAbstrata

class TelaTime(TelaAbstrata):

    def __int__(self):
        pass

    def dados_time(self):
        print("==== Cadastrar Time ====")
        nome = input("Nome do time: ")
        orcamento = input("orcamento: ")

        return {'nome': nome, 'orcamento': orcamento}

    def mensagem(self, msg):
        print("----- " + msg + " -----")

    def mensagem_erro(self, msg):
        print("#####" + msg + "#####")