# Crie um programa que leia uma lista de números do usuário e exiba o maior número dessa lista.
# Digitar os números
numeros = input("Digite uma sequência de números separados por espaço: ")

# Converter a sequêcia para lista e definir como float os números
numeros = [float(num) for num in numeros.split(",")]

# Definir o menor número
menor_numero = min(numeros)

# Exibe menor número
print("O menor número da lista é: ",menor_numero)