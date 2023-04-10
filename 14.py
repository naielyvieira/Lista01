# Crie um programa que leia uma lista de números do usuário e exiba somente os números maiores do que 10.      
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = numeros.split(",")

print("Os números maiores que 10 são: ")
for numero in numeros:
    if int(numero) > 10:
        print(numero)