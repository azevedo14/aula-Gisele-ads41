class Funcionario():
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def aumenta_salario(self, salario=0, valor=0):
        print(salario + valor)


class Programador(Funcionario):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade, salario)

    def aumenta_salario(self, valor=20):
        print("O salario do programador é:", self.salario + valor)


class Analista(Funcionario):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade, salario)

    def aumenta_salario(self, valor=30):
        print("O salario do analista é:", self.salario + valor)

class test():
    programador = Programador("guilherme", 18, 3500)
    programador.aumenta_salario()

    analista = Analista("joao", 18, 4000)
    analista.aumenta_salario()


test()
