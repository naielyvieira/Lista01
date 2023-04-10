# Crie um programa que leia uma lista de números do usuário e exiba o maior número dessa lista.
numeros = input("Insira uma lista de números separados por vírgula: ")

# Converte a entrada em uma lista de números inteiros
numeros = [int(num) for num in numeros.split(",")]

# Encontra o maior número na lista usando a função max()
maior_numero = max(numeros)

# Exibe o maior número na lista
print("O maior número na lista é:", maior_numero)