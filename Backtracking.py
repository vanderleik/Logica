# Backtracking

# Resolve recursivamente os problemas, tentando criar uma solução de forma incremental, uma peça de cada vez, removendo as soluções que falham em satisfazer as restrições do problema a qualquer momento.

# Encontrar toda a ordem possível de arranjos de um determinado conjunto de letras.
# Quando escolhemos um par, aplicamos Backtracking para verificar se esse par exato já foi criado ou não.
# Se ainda não tiver sido criado, o par será adicionado à lista de respostas, caso contrário, será ignorado.

# Função para o algoritmo Backtracking
def permuta(combinacoes, lista):
    # Verificamos se o número de combinações é igual a 1
    # e retornamos a própria lista, pois não há combinações a fazer
    if combinacoes == 1:
        return lista
    # Se quisermos mais de 1 combinação dos elementos, começamos a recursão
    else:
        # Usamos list comprehension com recursão (chamada à própria função)
        return [ y + x for y in permuta(1, lista) for x in permuta(combinacoes - 1, lista) ]

# Executa a função buscando diferentes combinações e aplicando a técnica de Backtracking
print(permuta(1, ["a","b","c"]))
print(permuta(2, ["a","b","c"]))
print(permuta(3, ["a","b","c"]))

permuta3 = permuta(3, ["a","b","c"])

print("São geradas",len(permuta3), "combinações entre a, b e c, quando combinamos as 3 letras.")