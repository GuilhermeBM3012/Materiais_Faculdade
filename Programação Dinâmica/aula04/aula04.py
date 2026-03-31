from collections import deque

fila_prioritaria = deque()
fila_padrao = deque()

def add_pessoa(pessoa):
    if pessoa['idade'] >= 65:
        fila_prioritaria.appendleft(pessoa)
    else:
        fila_padrao.appendleft(pessoa)
    return

p1 = {"nome": "Guilherme", "idade": 60}
p2 = {"nome": "Lucas", "idade": 70}

add_pessoa(p1)
add_pessoa(p2)

print("Prioritária:", fila_prioritaria)
print("Padrão:", fila_padrao)