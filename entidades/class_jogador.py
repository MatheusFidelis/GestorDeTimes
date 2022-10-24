class Jogador:
    
    def __init__(self, nome: str, camisa: int, posicao: str, idade: int, salario: float):
        self.__nome = nome
        self.__camisa = camisa
        self.__posicao = posicao
        self.__idade = idade
        self.__salario = salario  
        self.__status = bool