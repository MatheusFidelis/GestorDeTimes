from telas.tela_abstrata import TelaAbstrata


class TelaMenu(TelaAbstrata):

    def __init__(self):
        pass

    def opcoes(self):
        print(" --- Gerenciar Orçamento--- ")
        print("Escolha uma das opções:")
        print("1 - Checar orçamento")
        print("2 - Adicionar orçamento")
        print("3 - Listar despesas")
        print("0 - Voltar")

        opcao = input("Escolha uma das opções: ")
        return opcao