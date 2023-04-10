# Crie um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem crescente.
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = [int(num) for num in numeros.split(",")]  # converte a string em uma lista de inteiros

numeros.sort()  # ordena a lista em ordem crescente

print("A lista em ordem crescente é:", numeros)