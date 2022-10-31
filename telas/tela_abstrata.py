from abc import abstractmethod, ABC

class TelaAbstrata(ABC):
    #@abstractmethod
    def __init__(self):
        pass

    def mensagem(self, msg):
        print("----- " + msg + " -----")

    def mensagem_erro(self, msg):
        print("#####" + msg + "#####")