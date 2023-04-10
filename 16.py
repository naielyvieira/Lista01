# Crie um programa que leia uma lista de números do usuário e exiba a soma dos números pares.
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = [int(num) for num in numeros.split(",")]  # converte a string em uma lista de inteiros

soma_pares = 0
for num in numeros:
    if num % 2 == 0:  # verifica se o número é par
        soma_pares += num # inclementar os numeros e somá-los

print("A soma dos números pares é:", soma_pares)