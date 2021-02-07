""" Criar um programa e somar os dígitos de 1 a 5 usando recursividade:
(ou seja: 1 + 2 + 3 + 4 + 5 = 15).
"""

# Pseudocódigo:
# 1. Define a função de soma recursiva.
# 2. Se n > 0, a variável soma recebe o resultado da soma recursiva entre n-1 e n.
# 2.1. Caso n < 0, a variável soma recebe 0.
# 3. Retorna soma

# Código do progrmama:

# 1. Define a função de soma recursiva.
def somaRec(n):
    # 2. Se n > 0, a variável soma recebe o resultado da soma recursiva entre n-1 e n.
    if n > 0:
        soma = somaRec(n-1) + n
    # 2.1. Caso n < 0, a variável soma recebe 0.
    else:
        soma = 0
    # 3. Retorna soma
    return soma

soma1 = input("\nInforme a sequência de números a ser somada:")
soma1 = int(soma1)

somaRec(soma1)