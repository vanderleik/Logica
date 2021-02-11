# Programação dinâmica

# Para vários exemplos de programaçãço dinâmica acessar o link:
# https://www.geeksforgeeks.org/dynamic-programming/

# Programação Dinâmica - Partição de Strings

# Input: marceloachaqueoclimapodemudar

# Output: marcelo acha que o clima pode mudar

# Dicionário com as palavras disponíveis
dicionario = {
    "acha": True,
    "que": True,
    "o": True,
    "clima": True,
    "pode": True,
    "mudar": True
    }

# Função de custo
def calculaCusto(palavra):
    """Avalia o custo de uma determinada palavra.
    Retorna 0 se a palavra estiver no dicionário, ou o número de caracteres caso contrário.
    Argumentos:
    palavra (string): uma palavra cujo custo precisa ser avaliado.
    Retorno:
    O custo da palavra (int).
    """
    if palavra in dicionario:
        return 0
    else:
        return len(palavra)

# O cache para memorizar soluções parciais
# Aqui está a grande diferença da Programação Dinâmica, uma espécie de 
# "memória" para armazenar soluções parciais
cache = {}

# Função para dividir a string de input
def divideString(input_string, inicio_index):
    """Esta função recursiva, tenta dividir a substring começando em
    'inicio_index' em partições, ou seja, palavras!
    Argumentos:
        input_string (string): a string inicial que precisa ser dividida.
        inicio_index (int): queremos dividir a substring de input_string começando nesse índice
        Retorno:
            Uma forma de tupla da solução parcial e seu custo
    """
    # Já calculamos a solução ideal a partir do ponto
    if inicio_index in cache:
        return cache[inicio_index]
    # A substring para dividir
    substring = input_string[inicio_index:]
    # Estas são as condições de contorno
    # Se a substring estiver vazia, retorne uma string vazia sem nenhum custo
    if not len(substring):
        return '', 0
    min_cost = None
    min_string = None
    # Colocamos nossa próxima partição em algum lugar entre o início + 1 e o final do input_string
    for i in range(1, len(substring) + 1):
        # Dividimos o resto da string recursivamente
        rest_string, rest_cost = divideString(input_string, inicio_index + i)
        current_string = substring[:i]
        current_cost = calculaCusto(current_string) + rest_cost
        # Atualiza o custo mínimo e string, se for o melhor até agora
        if min_cost is None or current_cost < min_cost:
            # Se as duas partes não estiverem vazias, junte-as com espaço
            if current_string and rest_string:
                min_string = current_string + ' ' + rest_string
                # Adicionamos um custo ao espaço em branco para evitar a divisão de
                # palavras desconhecidas em pequenos pedaços
                current_cost += 1
            else:
                min_string = current_string + rest_string
                min_cost = current_cost
    cache[inicio_index] = min_string, min_cost
    return min_string, min_cost

# Executa a função começando do índice 0
print(divideString("marceloachaqueoclimapodemudar", 0))

Saída: ('marcelo acha que o clima pode mudar', 13)

# Executa a função começando do índice 7
print(divideString("marceloachaqueoclimapodemudar", 7))

Saída: ('acha que o clima pode mudar', 5)