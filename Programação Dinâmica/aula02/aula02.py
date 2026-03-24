from array import array

# 1-
numeros = array('i',[1,2,3,4,5,6,7,8,9])

def maior_e_menor(lista):
    maior_num = lista[0]
    menor_num = lista[0]

    for num in lista:
        if num > maior_num:
            maior_num = num

        if num < menor_num:
            menor_num = num

    print(f'O maior número é: {maior_num}\nO menor número é: {menor_num}')

maior_e_menor(numeros)


# 2-
numeros2 = array('i',[10, 2, 5, 4, 7, 20, 40, 50, 70])

def acha_elemento(lista, alvo):
    print(lista)

    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

resultado = acha_elemento(numeros, 2)
print(f'índice: {resultado}')


# 3-
numeros3 = array('i',[3, 5, 3, 2, 3, 8])

def cont_vezes_num(lista, alvo):
    cont = 0
    for num in lista:
        if num == alvo:
            cont += 1
    print(f'O número {alvo} apareceu {cont} vezes')

cont_vezes_num(numeros3, 3)


# 4-
numeros4 = array('i', [1, 2, 3, 0, 0])
size = 3

def inserir_no_espaco_livre(lista, size, valor):
    if size == len(lista):
        print('Erro!\nArray cheio')
        return size

    lista[size] = valor
    size += 1

    print(lista)
    return size

size = inserir_no_espaco_livre(numeros, size, 4)
size = inserir_no_espaco_livre(numeros, size, 5)


# 5-
numeros5 = array('i', [1,2,3,4,5])

def inverter_array(lista):
    fim = len(lista) - 1

    while lista[0] < fim:

        lista[0] = lista[fim]
        lista[fim] = lista[0]

        lista[0] += 1
        fim -= 1

    print(lista)
    return lista

inverter_array(numeros5)


# 6-
numeros6 = array('i',[2, 33, 4, 55, 66, 9, 2, 12, 0, 8, 35, 99, 1 ])

def ordena_array_estatico(lista):
    for i in range(len(lista)):
        contadorTrocas = 0
        for j in range(len(lista) - i - 1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i + 1] = aux
                contadorTrocas += 1

        if contadorTrocas == 0:
            break
    return lista

ex06 = ordena_array_estatico(numeros6)
print(ex06)


# 7-
numeros7 = array('i', [3,1,2,6,3,4,3])

def frequencia_dados(lista):

    cont = array('i', [0]*7)  # índices de 0 a 6

    for num in lista:
        cont[num] += 1

    for i in range(1, 7):
        print(f"{i} → {cont[i]}")


frequencia_dados(numeros7)


# 8-
numeros8 = array('i',[10, 20, 30, 40, 0])

def insert_sorted(lista, valor):
    pos = 0

    for i in range(len(lista) - 1):
        if valor > lista[i]:
            pos += 1

    for i in range(len(lista) - 1, pos, -1):
        lista[i] = lista[i-1]

    lista[pos] = valor
    print(lista)

insert_sorted(numeros8, 25)