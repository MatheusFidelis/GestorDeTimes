from telas.tela_abstrata import TelaAbstrata

class TelaElenco(TelaAbstrata):
    
    def __init__(self):
        pass
    
    def opcoes(self):
        print(" --- Gerenciar Elenco--- ")
        print("1 - Contratar Jogador")
        print("2 - Editar Informações do Jogador")
        print("3 - Listar Jogadores")
        print("4 - Rescindir Jogador")
        print("0 - Voltar")
    
        opcao = input("Escolha uma das opções: ")
        return opcao
    
    def dados_jogador(self):
        print("------- CADASTRAR JOGADOR -------")
        nome = input("Nome: ")
        idade = input("Idade: ")
        posicao = input("Posição: ")
        camisa = input("Camisa: ")
        salario =  input("Salario: ")


        
        return {"nome": nome, "idade": idade, "posicao": posicao, "camisa": camisa, "salario": salario}
    
    def dados_alterar(self):
        print("------- ALTERAR JOGADOR -------")
        nome = input("Nome: ")
        idade = input("Idade: ")
        posicao = input("Posição: ")
        camisa = input("Camisa: ")

        
        return {"nome": nome, "idade": idade, "posicao": posicao, "camisa": camisa}
    
    
    def seleciona(self):
        print("------- SELECIONAR JOGADOR -------")
        camisa = input("Camisa: ")
        return camisa
    
    def confirma_exclusao(self):
        print(" --- CONFIRMAR EXCLUSÃO --- ")
        print("0 - Confirmar")
        print("1 - Cancelar")
        
        opcao = input("Escolha uma das opções: ")
        return opcao
        
        
    
    def mostra_jogador(self, dados_jogador):
        print("------- {} -------".format(dados_jogador["nome"]))
        print("NOME: ", dados_jogador["nome"])
        print("IDADE: ", dados_jogador["idade"])
        print("POSIÇÃO: ", dados_jogador["posicao"])
        print("Camisa: ", dados_jogador["camisa"])
        print("Salario: ", dados_jogador["salario"])
        print("\n")
        