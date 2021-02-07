""" Criar um programa e somar os dígitos de 1 a 5:
(ou seja: 1 + 2 + 3 + 4 + 5 = 15).
"""

# Pseudocódigo:
# 1- Define e inicializa a variável soma com 0.
# 2- Para cada valor de i começando por 1, repetimos por n vezes:
# 2.1- A variável soma recebe seu próprio valor mais i
# 3- Retorna soma


# Código do progrmama:

# 1- Define e inicializa a variável soma com 0.
def soma(n):
    soma = 0
    # 2- Para cada valor de i começando por 1, repetimos por n vezes:
    for i in range(n+1):
        # 2.1- A variável soma recebe seu próprio valor mais i
        soma = soma + i
# 3- Retorna soma
    return soma

soma1 = input("\nInforme a sequência de números a ser somada:")
soma1 = int(soma1)

soma(soma1)

# Usando o loop while

# Código do programa

def soma(n):
    soma = 0
    i = 1
    while i <= n:
        soma = soma + i
        i = i + 1
    return soma

soma1 = input("\nInforme a sequência de números a ser somada:")
soma1 = int(soma1)
soma(soma1)