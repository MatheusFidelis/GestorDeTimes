from telas.tela_abstrata import TelaAbstrata

class TelaMenu(TelaAbstrata):
    
    def __init__(self):
        pass
    
    def opcoes(self):
        print(" --- Menu principal --- ")
        print("Escolha uma das opções")
        print("1 - Gerenciar Elenco")
        print("2 - Gerenciar Orçamento")
        print("0 - Finalizar Sistema")
    
        opcao = input("Escolha uma das opções: ")
        return opcao