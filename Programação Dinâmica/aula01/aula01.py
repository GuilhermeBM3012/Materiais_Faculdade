import time
import random

tempo_inicial = time.time()
'''for i in range(100):
    pass
print('Tempo decorrido: ', time.time() - tempo_inicial)'''

count = 0

# 1
def getlast(n):
    global count
    count += 1
    return n[len(n) - 1]
    
lista1 = [i for i in range(10000)]

tempo_inicial = time.time()
print(getlast(lista1))

print('Função executada: ', count, ' vez(es)')
print('Tempo decorrido: ', time.time() - tempo_inicial)
# R: O(1)

# 2
def count_pairs_equal(a):
    global count
    c = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            count += 1
            if a[i] == a[j]:
                c += 1
    return c
lista2 = [random.randint(0, 100) for _ in range(100)]

tempo_inicial = time.time()
print(count_pairs_equal(lista2))

print('Função executada: ', count, ' vez(es)')
print('Tempo decorrido: ', time.time() - tempo_inicial)
# R: O(n^2)

# 3
def has_zero_sum_triple(a):
    global count
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                count += 1
                if a[i] + a[j] + a[k] == 0:
                    return True
    return False

lista3 = [random.randint(-100, 100) for _ in range(100)]

tempo_inicial = time.time()
print(has_zero_sum_triple(lista3))

print('Função executada: ', count, ' vez(es)')
print('Tempo decorrido: ', time.time() - tempo_inicial)
# R: O(n^3)

# 4
def some_search(a, target):
    global count
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        count += 1
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

lista4 = sorted([random.randint(0, 10000) for _ in range(10000)])
target = lista4[500]

tempo_inicial = time.time()
print(some_search(lista4, target))

print('Função executada:', count, 'vez(es)')
print('Tempo decorrido:', time.time() - tempo_inicial)
# R: O(log(n))

# 5
def fib(n):
    global count
    count += 1
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

tempo_inicial = time.time()
print(fib(20000))

print('Função executada:', count, 'vez(es)')
print('Tempo decorrido:', time.time() - tempo_inicial)
# R: O(2^n)

# 6
def common_prefix(words):
    global count
    if not words:
        return ""
    p = words[0]
    for w in words[1:]:
        while not w.startswith(p):
            count += 1
            p = p[:-1]
            if p == "":
                return ""
    return p

lista6 = ["flower", "flow", "flight"]

tempo_inicial = time.time()
print(common_prefix(lista6))

print('Função executada:', count, 'vez(es)')
print('Tempo decorrido:', time.time() - tempo_inicial)
# R: O(n * m)

# 7
def count_hits(sorted_a, queries):
    global count
    hits = 0
    for q in queries:
        count += 1
        if binary_search(sorted_a, q) != -1:
            hits += 1
    return hits

lista7 = sorted([random.randint(0, 10000) for _ in range(1000)])
queries = [random.randint(0, 10000) for _ in range(100)]

tempo_inicial = time.time()
print(count_hits(lista7, queries))

print('Função executada:', count, 'vez(es)')
print('Tempo decorrido:', time.time() - tempo_inicial)
# R: O(q log(n))

# 8
def factorial(n):
    global count
    count += 1
    
    if n <= 1:
        return 1
    return n * factorial(n - 1)

tempo_inicial = time.time()
print(factorial(1000))

print('Função executada:', count, 'vez(es)')
print('Tempo decorrido:', time.time() - tempo_inicial)

# R: O(n)

# 9
def bubble_sort(a):
    global count
    a = a[:] # cópia
    n = len(a)
    for i in range(n):
        for j in range(0, n - 1 - i):
            count += 1
            if a[j] > a[j + 1:
                a[j], a[j + 1] == a[j + 1], a[j],
    return a


lista9 = [random.randint(0, 1000) for _ in range(100)]

tempo_inicial = time.time()
print(bubble_sort(lista9))

print('Função executada:', count, 'vez(es)')
print('Tempo decorrido:', time.time() - tempo_inicial)
# R: O(n^2)

# 10
def perm(n):
    global count
    count += 1
    if n == 0:
        return 1
    total = 0
    for i in range(n):
        total += perm(n - 1)
    return total

tempo_inicial = time.time()
print(perm(6000))

print('Função executada:', count, 'vez(es)')
print('Tempo decorrido:', time.time() - tempo_inicial)
# R: O(n!)
