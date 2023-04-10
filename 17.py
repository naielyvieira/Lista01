# Crie um programa que leia uma lista de números do usuário e exiba a soma dos números ímpares.
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = [int(num) for num in numeros.split(",")]  # converte a string em uma lista de inteiros

soma_impares = 0
for num in numeros:
    if num % 2 != 0:  # verifica se o número é ímpar
        soma_impares += num # inclementar os numeros e somá-los

print("A soma dos números ímpares é:", soma_impares)
