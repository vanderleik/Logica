# Criar uma função capaz de determinar qual valor é maior entre dois números determinados.

# Pseudo-Código

# 1. Defina n1 como sendo o primeiro número
# 2. Defina n2 como sendo o segundo número
# 3. Estabeleça a condição de que:
# 3.1. se n1 > n2, então n1 é maior que n2.
# 3.2. se n1 < n2, então n2 é maior que n1.

# Código do programa

# Solução 01

enter = input("Pressione <Enter> para iniciar...")
# 1. Defina n1 como sendo o primeiro número
n1 = input("\nInforme o primeiro valor:")
n1 = int(n1)

# 2. Defina n2 como sendo o segundo número
n2 = input("\nInforme o segundo valor:")
n2 = int(n2)

# 3. Estabeleça a condição de que:
# 3.1. se n1 > n2, então n1 é maior que n2.
if n1 > n2:
    print(n1, "é maior que ",n2)
# 3.2. se n1 < n2, então n2 é maior que n1.
elif n2 > n1:
    print(n2, "é maior que ",n1)
else:
    print(n1, "é igual a ",n2)

# Solução 02, adaptada da aula.
# Essa solução não prevê que os números de entrada podem ser iguais!

enter = input("\nPressione <Enter> para executar novamente o programa com outro código de programação...")

def maximo2(a, b):
    if a > b:
        return a
    else:
        return b

# 1. Defina a como sendo o primeiro número
a = input("\nInforme o valor de a:")
a = int(a)

# 2. Defina b como sendo o segundo número
b = input("\nInforme o valor de b:")
b = int(b)

# 3. Estabeleça a condição de que:
# 3.1. se a > b, então a é maior que b.
# 3.2. se a < b, então b é maior que a.

print("\nO maior valor entre",a, "e", b, "é", maximo2(a, b))

enter = input("\nPressione <Enter> para executar outro programa, que encontrará o valor máximo entre 3 números...")

# Pseudo-Código para obter valor máximo entre 3 números

# 1. Leia 3 números representados por a, b e c.
# 2. Se a > b e b > c; retorne a.
# 3. Se a < b e b > c; retorne b.
# 4. Se as condições acima não forem satisfeitas, retorne c.

# Código do programa

# Solução 01

# 1. Leia 3 números representados por a, b e c.
def maximo3(a, b, c):
    # 2. Se a > b e b > c; retorne a.
    if a > b and b > c:
        print("O maior valor é", a)
    # 3. Se a < b e b > c; retorne b.
    elif a < b and b > c:
        print("O marior valor é ", b)
    # 4. Se as condições acima não forem satisfeitas, retorne c.
    else:
        print("O maior valor é", c)

a = input("\nInforme o valor de a:")
a = int(a)

b = input("\nInforme o valor de b:")
b = int(b)

c = input("\nInforme o valor de c:")
c = int(c)

maximo3(a, b, c)

enter = input("\nPressione <Enter> para entrar novamente com os valores e ver outra solução...")

# Solução 02

# 1. Leia 3 números representados por a, b e c.
def maximo3_v2(a, b, c):
    if a < b:
        return maximo2(b, c)
    else:
        return maximo2(a, c)

a = input("\nInforme o valor de a:")
a = int(a)

b = input("\nInforme o valor de b:")
b = int(b)

c = input("\nInforme o valor de c:")
c = int(c)

print("O maior valor é:", maximo3_v2(a, b, c))

enter = input("\nPressione <Enter> para encerrar...")