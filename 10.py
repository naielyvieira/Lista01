#Crie um programa que leia uma lista de números do usuário e exiba a média desses números.
# Definir variavel
def calcular_media(lista):
    if len(lista) == 0:
        return 0
    else:
        return sum(lista) / len(lista)

# Lê a lista de números do usuário
numeros = input("Digite uma lista de números separados por vírgula: ")
numeros = numeros.split(",")
numeros = [float(numero) for numero in numeros]

# Calcula a média e exibe o resultado
media = calcular_media(numeros)
print("A média dos números é:", media)