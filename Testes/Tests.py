class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf # privado

    def setidade(self,num):
        self.idade = num

    def setnome(self,nome):
        self.nome = nome

    def getcpf(self):
        return self.__cpf

    def mudarcpf(self, cpf):
        self.__cpf = cpf


ana = Pessoa('Ana', 20, '987654321')

ana_cpf = ana.getcpf()
print(ana_cpf)

ana.mudarcpf(5664)

ana_cpf = ana.getcpf()

print(ana_cpf)