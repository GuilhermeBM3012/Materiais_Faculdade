# 1
def inverte_string(texto):
    lista = []

    for char in texto:
        lista.append(char)

    palavra_invertida = ''

    while lista:
        palavra_invertida += lista.pop()

    return palavra_invertida

print(inverte_string('palavra'))


# 2
def inverte_texto(texto):
    lista = []
    texto = texto.upper()

    for sinais in ',.;:?':
        texto = texto.replace(sinais, '')

    for char in texto:
        lista.append(char)

    palavra_invertida = ''

    while lista:
        palavra_invertida += lista.pop()

    if palavra_invertida == texto:
        print(f'O texto: {texto} é um palíndromo!')
    else:
        print(f'O texto: {texto} não é um palíndromo!')
    return palavra_invertida

inverte_texto('Amor a roma')


# 3
def verificar_comandos(lista):
    resultado = []

    for comando in lista:
        if comando == "UNDO":
            if len(resultado) > 0:
                resultado.pop()
        else:
            resultado.append(comando)

    return resultado

entrada = ["A", "B", "C", "UNDO", "D"]
print(verificar_comandos(entrada))


# 4
def remove_pares_iguais(texto)
    lista = []
    for char in texto:
        if len(lista) > 0 and lista[-1] == char:
            pilha.pop()
        else:
            pilha.append(char)

entrada = 'abbaca'
print(remove_pares_iguais(entrada))


# 5
def verificar_parenteses_balanceados():
    lista = []
    for char in expressao:
        if char == "(":
            lista.append(char)
        elif char == ")":
            if len(lista) == 0:
                return False
            lista.pop()

    return len(lista) == 0

expr = input("Digite a expressão: ")

if verificar_parenteses_balanceados(expr):
    print("Parênteses balanceados ✔")
else:
    print("Parênteses NÃO balanceados ❌")          


# 6
def decimal_para_binario(numero):
    lista = []

    while numero > 0:
        resto = numero % 2
        lista.append(resto)
        numero = numero // 2

    binario = ''

    while len(lista) > 0:
        binario += str(lista.pop())

    return binario

num = int(input('Digite um número decimal: '))
print(f'Binário de {num}', decimal_para_binario(num))
