# Crie um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem decrescente.
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = [int(num) for num in numeros.split(",")]  # converte a string em uma lista de inteiros

numeros.sort(reverse=True)  # ordena a lista em ordem decrescente

print("A lista em ordem decrescente é:", numeros)