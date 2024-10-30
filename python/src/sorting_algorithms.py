import random
import time
from typing import List

lista_ordenada = [0, 2, 5, 13, 40, 52, 66, 79, 81, 95]


# gera uma lista aleatória com `num` números entre `min` e `max`
def lista_aleatoria(min: int, max: int, num: int) -> List[int]:
    return [] if max <= min else random.sample(range(min, max), num)


# itera até o próximo elemento que seja maior que si mesmo
def selection_sort(lista):
    length = len(lista)
    for i in range(length):
        min = i
        for j in range(i + 1, length):
            if lista[j] < lista[min]:
                min = j
        lista[i], lista[min] = lista[min], lista[i]
    return lista


# itera em pares, verificando se o elemento seguinte (atual + 1) é maior que o atual
def bubble_sort(lista):
    length = len(lista)
    for i in range(length):
        for j in range(length - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


# elemento por elemento, verifica na lista de elementos ordenados qual espaço mais adequado
def insertion_sort(lista):
    length = len(lista)
    for i in range(1, length):
        chave = lista[i]
        k = i
        while k > 0 and chave < lista[k - 1]:
            lista[k] = lista[k - 1]
            k -= 1
        lista[k] = chave
    return lista


# busca binária em lista ordenada, retornando a posição do elemento procurado
def busca_binaria(seq, item):
    inicio = 0
    final = len(seq) + 1

    while inicio <= final:
        meio = (inicio + final) // 2

        if seq[meio] < item:
            inicio = meio + 1
        elif seq[meio] > item:
            inicio = meio - 1
        else:
            return meio


# concatena de forma ordenada duas listas diferentes
# (usado pelo merge_sort)
def merge(left, right):
    l_index = r_index = 0
    result = []
    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            result.append(left[l_index])
            l_index += 1
        else:
            result.append(right[r_index])
            r_index += 1

    result += left[l_index:]
    result += right[r_index:]
    return result


# ordena a lista recursivamente dividindo-a ao meio e utilizando a função merge
def merge_sort(lista):
    length = len(lista)
    if length <= 1:
        return lista

    half = length // 2
    left = merge_sort(lista[:half])
    right = merge_sort(lista[half:])

    return merge(left, right)


# gera uma lista aleatória com 1000 elementos e executa cada algoritmo nela
lista_gerada = lista_aleatoria(-1000, 1000, 1000)
# print(f"Lista desordenada: {lista_gerada}")
for sort_function in [bubble_sort, selection_sort, insertion_sort, merge_sort]:
    start_time = time.perf_counter()
    sorted = sort_function(lista_gerada[:])
    end_time = time.perf_counter()
    print(f"{sort_function.__name__}: - (t: {(end_time - start_time):.4f})")
