# Crie um programa que leia uma lista de números do usuário e exiba somente os números pares.
numeros = input("Digite uma sequêcia de números separados por vírgula: ")
numeros = numeros.split(",")

print("Os números pares são: ")
for numero in numeros:
    if int(numero) % 2 == 0:
        print(numero)
        