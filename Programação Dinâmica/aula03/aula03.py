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
