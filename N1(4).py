import datetime
from random import randint

def calculo_tempo(function):
    def calculo():
        print(datetime.datetime.now())

        function()

        print(datetime.datetime.now())

    return calculo()

lista = []
while len(lista) < 4:
    numero = randint(1, 100)
    lista.append(numero)
print(lista)

@calculo_tempo
def funcao():
    soma = 0
    for a in lista:
        soma += a
    print(soma)

funcao

# Decorator é um padrão de software, ele permite adicionar e modificar um comportamendo de um objeto, classe ou funçõo dinamicamente,responsavel por adicionar
# a um objeto funções as quais antes não pertenciam a ele em tempo de execução. Decorators oferecem uma alternativa flexível
# ao uso de herança para estender uma funcionalidade, com isso adiciona-se uma responsabilidade ao objeto e não à classe.

#Padrões de projeto são conhecidos como a solução que ja foi testada para um problema, nessa forma reutilizamos a experiência
#de outros desenvolvedores que tiveram probLemas semelhantes. Dessa forma, um padrão de projeto geralemente descreve uma solução ou uma instancia da solução
#que foi utilizada para desenvolver um problema especifico.
