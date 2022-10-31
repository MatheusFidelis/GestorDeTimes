class Jogador:
    
    def __init__(self, nome: str, camisa: int, posicao: str, idade: int, contrato):
        self.__nome = nome
        self.__camisa = camisa
        self.__posicao = posicao
        self.__idade = idade
        self.__contrato = contrato
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
        
    @property
    def camisa(self):
        return self.__camisa
    
    @camisa.setter
    def camisa(self, camisa: int):
        self.__camisa = camisa
            
    @property
    def posicao(self):
        return self.__posicao
    
    @posicao.setter
    def posicao(self, posicao: str):
        self.__posicao = posicao
            
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade: int):
        self.__idade = idade

    @property
    def contrato(self):
        return self.__contrato

    @contrato.setter
    def contrato(self, contrato):
        self.__contrato = contrato
