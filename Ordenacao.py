# Aula 07 - Ordenação

# Ordenação Por Bolha (Bubble Sort)

1. Se o elemento i > j, troca deposição entre i e j;
2. Se o elemento i < j, não faz nada.

def bubble_sort(lista):
    # Função que realiza a troca dos elementos
    def troca(i, j):
        lista[i], lista[j] = lista[j], lista[i]
    n = len(lista)
    trocado = True
    x = -1
    while trocado:
        trocado = False
        x = x + 1
        for i in range(1, n - x):
            if lista[i - 1] > lista[i]:
                troca(i - 1, i)
                trocado = True
    return lista

# Lista não ordenada
listaNum = [9, 3, 5, 4, 6, 2, 7, 1, 8]

# Ordena a lista
bubble_sort(listaNum)

# Encontrei outra forma de fazer o mesmo código no Stack Overflow.
# A diferença é que ele lista todas as trocas de elementos dentro da lista.

def bubble_sort1(lista):
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

# Lista não ordenada
listaNum1 = [9, 3, 5, 4, 6, 2, 7, 1, 8]

# Ordena a lista
bubble_sort1(listaNum1)

# Ordenação Por Seleção (Selection Sort)

import random

random.seed(6)

A = random.sample(range(-10, 10), 10)
print("Arranjo não ordenado: ", A)

def ordenacao_selecao(A):
    n = len(A)
    # Percorre o arranjo A
    for i in range(n):
        # Encontra o elemento mínimo em A
        minimo = i
        for j in range(i + 1, n):
            if A[minimo] > A[j]:
                minimo = j
        # Coloca o elemento minimo na posição correta
        A[i], A[minimo] = A[minimo], A[i]

ordenacao_selecao(A)
print("Arranjo ordenado", A)

# Ordenação Por Mistura (Merge Sort)
# Dividir e conquistar
# Esse código é da Wikipedia (mas não conta pra ninguém!)

def mergeSort(lista):
    if len(lista) > 1:
        # Dividir
        meio = len(lista)//2
        #também é valido: meio = int(len(lista)/2)
        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]
        mergeSort(listaDaEsquerda)
        mergeSort(listaDaDireita)

        i = 0
        j = 0
        k = 0

        while i < len(listaDaEsquerda) and j < len(listaDaDireita):
            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1

        while i < len(listaDaEsquerda):
            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1

B = random.sample(range(-10, 10), 10)
print("Arranjo não ordenado: ", B)

mergeSort(B)
print("Arranjo ordenado:", B)

# Ordenação Rápida (Quick Sort)
# Dividir e conquistar

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    # Marcadores de posição, leftmark e rightmark
    leftmark = first+1
    rightmark = last

    done = False
    while not done:
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

       if rightmark < leftmark:
            done = True
       else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp


    return rightmark

C = random.sample(range(-10, 10), 10)
print("Arranjo não ordenado: ", C)

quickSort(C)
print("Arranjo ordenado:", C)

