# Algoritmos Gulosos (Greedy Algorithms)

# Para uma lista de algoritimos gulosos:
# https://www.geeksforgeeks.org/greedy-algorithms/

# Neste exato momento, qual é a melhor escolha a ser feita?

# Você precisa consumir 1.000 calorias/dia de uma lista de 10 alimentos.

Alimentos = ['Frango', 'Milk Shake', 'Pizza', 'Hamburger', 'Batata Frita', 'Refrigerante', 'Maça', 'Laranja', 'Cenoura', "Alface"]

Valores = [79, 18, 45, 38, 25, 9, 15, 10, 22, 12] # Em reais

Calorias = [114, 156, 359, 354, 365, 153, 97, 82, 79, 40]

# Algoritmo para buscar as melhores combinações de cardápio considerando duas regras
# (constraints): valor do cardápio para 1000 calorias e custo do cardápio para 1000 calorias

# Algoritmo guloso que busca a melhor combinação de alimentos para uma dieta de 1000 calorias.

# Classe para armazenar os alimentos
class Alimentos(object):
    # Construtor da classe
    def __init__(self, n, v, c):
        # Nome do alimento
        self.nome = n
        # Valor do alimento em Reais
        self.valor = v
        # Número de calorias do alimento
        self.calorias = c
    # Método para obter o valor de cada alimento
    def getValor(self):
        return self.valor
    # Método para obter o custo (1 dividido pelo número de calorias, calculado mais abaixo. Aqui retornamos apenas as calorias)
    def getCusto(self):
        return self.calorias
    # Método para imprimir nome/valor/calorias
    def __str__(self):
        return self.nome + ': <' + str(self.valor) + ', ' + str(self.calorias) + '>'

# Cria o Menu com a lista de alimentos"
def criaMenu(nomes, valores, calorias):
    # Cria a lista vazia
    menu = []
    # De acordo com o tamanho da lista de valores, inserimos todos os itens na lista de menu
    for i in range(len(valores)):
        menu.append(Alimentos(nomes[i], valores[i], calorias[i]))
    return menu

# Algoritmo Guloso
def greedy(items, maxCost, keyFunction):
    # Copia todos os itens
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    # Lista de resultados
    resultado = []
    # Valor total
    totalValor = 0
    # Custo total
    totalCusto = 0.0
    # De acordo com o tamanho da lista de itens, realiza os seguintes cálculos
    for i in range(len(itemsCopy)):
        if (totalCusto + itemsCopy[i].getCusto()) <= maxCost:
            # adiciona os itens a lista de resultados
            resultado.append(itemsCopy[i])
            # Calcula o custo total
            totalCusto += itemsCopy[i].getCusto()
            # Calcula o valor total
            totalValor += itemsCopy[i].getValor()
    return (resultado, totalValor)

# Função para executar o algoritmo guloso
def executaGreedy(items, constraint, keyFunction):
    result, val = greedy(items, constraint, keyFunction)
    print('Valor Total dos Itens para 1000 calorias =', val)
    for item in result:
        print(item)

# Função que gera o melhor cardápio pelo valor individual dos alimentos e pelo custo dos alimentos
def geraCardapio(alimentos, totCalorias):
    print('Usando o algoritmo guloso para buscar o melhor menu pelo valor dos alimentos para', totCalorias, 'calorias')
    executaGreedy(alimentos, totCalorias, Alimentos.getValor)
    print('\nUsando o algoritmo guloso para buscar o melhor menu pelo custo dos alimentos para', totCalorias, 'calorias')
    executaGreedy(alimentos, totCalorias, lambda x: 1/Alimentos.getCusto(x))

# Listas para testar o algoritmo
listaAlimentos = ['Frango', 'Milk Shake', 'Pizza', 'Hamburger', 'Batata Frita', 'Refrigerante', 'Maça', 'Laranja', 'Cenoura', "Alface"]
valores = [79, 18, 45, 38, 25, 9, 15, 10, 22, 12]
calorias = [114, 156, 359, 354, 365, 153, 97, 82, 79, 40]

# Cria o menu
menu_alimentos = criaMenu(listaAlimentos, valores, calorias)

# Busca o melhor menu para o consumo de 1000 calorias
geraCardapio(menu_alimentos, 1000)
