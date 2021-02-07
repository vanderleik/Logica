"""
Os números de Fibonacci compõem a seguinte sequência:
0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, ...
Em termos matemáticos:
Fn = Fn-1 + Fn-2
"""
# Pseudo-código
# 1 Definir uma variável "n" que representa a posição do número na Sequência de Fibonacci.
# 2 Se "n" < 0, será inválido (não tem posição negativa).
# 3 Se "n" > = 0, verificar se "n" == 1. Se "n" == 1, retorna 0 (primeiro valor na Sequência de Fibonacci).
# Se "n" > = 1, verificar se "n" == 2. Se "n" == 2, retorna 1 (segundo valor na Sequência de Fibonacci).
# Se "n" não estiver em nenhuma das condições anteriores, usar a regra Fn = Fn-1 + Fn-2 para encontrar a posição de "n".

# Código do Programa

def encontraFibonacci(n):
    if n < 0:
        print("Entrada incorreta!")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return encontraFibonacci(n-1) + encontraFibonacci(n-2)

posicao = input("Informe a posição a ser obtida na Sequência Fibonacci:")
posicao = int(posicao)
print(encontraFibonacci(posicao))