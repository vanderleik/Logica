""" 
Devo imprimir todos os valores da Sequência de Fibonacci até a posição que eu vou especificar na Sequência de Fibonacci (SF).
""" 

"""
Os números de Fibonacci compõem a seguinte sequência:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, ...
Em termos matemáticos:
Fn = Fn-1 + Fn-2
"""

# Pseudocódigo:

# 1. n = a posição desejada na SF.
# 2. n1 = valor da primeira posição na SF.
# 3. n2 = valor da segunda posição na SF.
# 4. count = contador. Serve para saber quando chegamos ao fim da SF até o valor de n.
# 5. Se n < 0, imprima mensagem na tela indicando que n não pode ser negativo, pois não temos posição negativa na SF.
# 6. Se n == 1, imprime n1.
# 7. Caso as condições 5 e 6 não forem satisfeitas, repetimos os passos abaixo enquanto count < n:
# 7.1. Imprime n1 na tela.
# 7.2. Próximo valor = n1 + n2.
# 7.3. n1 = n2.
# 7.4. n2 = valor calculado em 7.2.
# 7.5. Incrementa o contador.

# Iniciando a programação

# 1. n = a posição desejada na SF. (Devo informar até qual posição desejo gerar a SF)
n = input("Informe até qual posição você deseja obter a Sequência Fibonacci:")
n = int(n)

# 2. n1 = valor da primeira posição na SF. (O valor de n1 = 0, porque o primeiro número da Sequência de Fibonacci é 0).
n1 = 0

# 3. n2 = valor da segunda posição na SF. (O valor de n2 = 1,  porque o segundo número da Sequência de Fibonacci é 1)
n2 = 1

# 4. count = contador. Serve para saber quando chegamos ao fim da SF até o valor de n.
count = 0

# 5. Se n < 0, imprima mensagem na tela indicando que n não pode ser negativo, pois não temos posição negativa na SF.
if n < 0:
    print("A posição não pode ser negativa.")
    # 6. Se n == 1, imprime n1.
elif n == 1:
    print("A Sequência de Fibonacci até ", n, " :")
    print(n1)
    # 7. Caso as condições 5 e 6 não forem satisfeitas, repetimos os passos abaixo enquanto count < n:
else:
    print("A Sequência de Fibonacci até ", n, " :")
    while count < n:
        # 7.1. Imprime n1 na tela.
        print(n1, end = ',')
        # 7.2. Próximo valor = n1 + n2.
        nth = n1 + n2
        # 7.3. n1 = n2.
        n1 = n2
        # 7.4. n2 = valor calculado em 7.2.
        n2 = nth
        # 7.5. Incrementa o contador.
        count += 1
