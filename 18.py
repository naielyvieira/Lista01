#Crie um programa que leia uma lista de números do usuário e exiba o produto desses números.
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = [int(num) for num in numeros.split(",")]  # converte a string em uma lista de inteiros

produto = 1
for num in numeros:
    produto *= num

print("O produto dos números é:", produto)