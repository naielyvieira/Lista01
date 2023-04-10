# Crie um programa que leia uma lista de números do usuário e exiba somente os números ímpares
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = numeros.split(",")

print("Os números ímpares são: ")
for numero in numeros:
    if int(numero) % 2 != 0:
        print(numero)