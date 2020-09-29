lista = []
while True:
    recebe_lista = int(input(
        "digite os numeros de rebeldes ou digite 0 para sair: "))
    if recebe_lista > 0:
        lista.append(recebe_lista)
    else:
        print(lista)
        break

def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False
        print(lista)
    return lista

def media(l):
    soma = 0
    for a in l:
        soma = soma + a

    media = soma / len(lista)
    return media

def comparacao(list):

    avg = sum(list) / len(list)
    diffs = {value: abs(value - avg) for value in list}

    return min(diffs, key=diffs.get)

bubble_sort(lista)
print(lista)
print("esse é o menor numero", lista[0])
print("esse é o maior numero", lista[len(lista)-1])
print("essa é a media", media(lista))
print("esse é o numero mais proximo da media", comparacao(lista))
