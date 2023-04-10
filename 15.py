# Crie um programa que leia uma lista de números do usuário e exiba somente os números menores do que 5.
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = [int(num) for num in numeros.split(",")]  # converte a string em uma lista de inteiros

print("Números menores do que 5:")
for num in numeros:
    if num < 5:
        print(num)