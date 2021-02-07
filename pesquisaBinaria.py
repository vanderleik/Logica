"""
Desejo encontrar o elemento x dentro de um vetor de tamanho n.

Suponha x = 72 (esse é o elemento que eu quero encontrar) e que:
v = [2,6,35,49,56,72,94].

Para fazer a busca vou utilizar uma pesquisa binária recursiva. Para isso, preciso definir três ponteiros: Left, Middle e Right.

Se o valor buscado for igual ao valor da posição Middle, o algoritmo retorna o valor buscado, ou sua posição. 
Se o valor buscado > Middle, desloco o ponteiro Left para Middle + 1. 
Se o valor buscado < Middle, desloco o ponteiro Right para Middle - 1.

Faço isso sucessivamente até localizar o valor alvo.

# Pseudo-código
# Achei mais intuitiva a explicação do: https://medium.com/@fellipetavaresft/algoritmo-de-pesquisa-bin%C3%A1ria-em-python-2aa94f7f41ed
# Por isso eu peguei o pseudo-código de lá.

1 - Defina Left = 0, Right = n-1; (onde n é o tamanho do vetor).
2 - Calcule Middle como a média de left e rigth, e arredonde sempre para baixo, para um valor inteiro.
3 - Se array[middle] = valor buscado, então pare a iteração. Você achou o valor buscado! Retorne Middle.
4 - Se array[middle] < valor buscado, defina Left = Middle + 1.
5 - Se array[middle] > valor buscado, defina Right = Middle - 1.
6 - volte ao passo 2.
"""

# Programa Python para pesquisa binária recursiva, usando o código do Fellipe Tavares.
# Porém, se você olhar os passos 4 e 5 do algorítimo, perceberá que o autor inverteu os sinais + e - no código!

def binarySearch(array, key):
    length = len(array)
    left = 0
    right = length - 1
  
    while(left <= right):
        middle = int((left + right)/2)
        if array[middle] == key:
            print (middle)
            break
        if key < array[middle]:
            right = middle - 1
        if key > array[middle]:
            left = middle + 1
    else:
        print("Value not found")

x = [1,2,3,4,5,6,7,8,9,10]
y = 2

binarySearch(x,y)


# Código segundo o curso da DSA

def pesquisaBinaria (vetor, left, right, x):
    # Verifica se a última posição do vetor é maior ou igual a 1 para garantir
    # # que tenhamos um vetor de comprimento maior que zero
    if right >= left:
        middle = left + (right - left) // 2
        # Se o elemento estiver presente no meio em si
        if vetor[middle] == x:
            return middle
        # Se o elemento for menor que o meio, ele poderá estar presente apenas no sub-vetor esquerdo
        elif vetor[middle] > x:
            return pesquisaBinaria(vetor, left, middle-1, x)
    # Senão, o elemento pode estar presente apenas no sub-vetor direito
        else:
            return pesquisaBinaria(vetor, middle + 1, right, x)
    else:
        # O elemento não está presente na matriz
        return -1

# Vetor de teste
listaNum = [ 12, 13, 40, 56, 93 ]
x = 56
# Chamada da função
resultado = pesquisaBinaria(listaNum, 0, len(listaNum)-1, x)

if resultado != -1:
    print ("O elemento está presente no índice %d!" % resultado)
else:
    print ("O elemento não está presente no vetor!")



""" Exercício: Dada a lista de famosos autores brasileiros, crie um programa que pesquise se "Clarice Lispector" está na lista e se estiver indique o índice da posição na lista. 

Aqui está a lista:
autores = ['Monteiro Lobato', 'José de Alencar', 'Cecília Meireles', 'Carlos Drummond de Andrade', 'Machado de Assis', 'Clarice Lispector', 'Graciliano Ramos', 'Guimarães Rosa', 'Ruth Rocha', 'Luis Fernando Veríssimo']
"""

# Pseudo-Código

# 1. Ordene a lista (porque a pesquisa binária tem como premissa que a lista esteja ordenada).
# 2. Defina Left = 0, Right = n-1; (onde n é o tamanho do vetor).
# 3. Calcule Middle como a média de left e rigth, e arredonde sempre para baixo, para um valor inteiro.
# 4. Se lista[middle] = valor buscado, então pare a iteração. Você achou o valor buscado! Retorne Middle.
# 5. Se lista[middle] < valor buscado, defina Left = Middle + 1.
# 6. Se lista[middle] > valor buscado, defina Right = Middle - 1.
# 7. volte ao passo 2.

# Código do programa

# 1. Ordene a lista (porque a pesquisa binária tem como premissa que a lista esteja ordenada).

autores = ['Monteiro Lobato', 'José de Alencar', 'Cecília Meireles', 'Carlos Drummond de Andrade', 'Machado de Assis', 'Clarice Lispector', 'Graciliano Ramos', 'Guimarães Rosa', 'Ruth Rocha', 'Luis Fernando Veríssimo']
autores.sort(reverse=False)
print(autores)
clarice = "Clarice Lispector" # Essa é a chave

# 2. Defina Left = 0, Right = n-1; (onde n é o tamanho do vetor).
def binarySearch(lista, chave):
    length = len(lista)
    left = 0
    right = length - 1
# 3. Calcule Middle como a média de left e rigth, e arredonde sempre para baixo, para um valor inteiro.  
# 4. Se lista[middle] = valor buscado, então pare a iteração. Você achou o valor buscado! Retorne Middle.
    while(left <= right):
        middle = int((left + right)/2)
        if lista[middle] == chave:
            print (middle)
            break
        # 5. Se lista[middle] < valor buscado, defina Left = Middle + 1.
        if chave > lista[middle]:
            left = middle + 1
        # 6. Se lista[middle] > valor buscado, defina Right = Middle - 1.
        # 7. volte ao passo 2.
        if chave < lista[middle]:
            right = middle - 1
    else:
        print("Value not found")

binarySearch(autores, clarice)
