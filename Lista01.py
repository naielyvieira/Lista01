# Crie um programa que solicite ao usuário o seu nome e exiba uma mensagem de boas-vindas.
nome = input("Qual é o seu nome? ")
print("Olá, " + nome + ", seja bem vindo(a)!")

# Crie um programa que leia dois números do usuário e exiba a soma desses números.

# Lê o primeiro número do usuário:
num1 = float(input("Digite um número: "))

# Lê segundo número do usuário:
num2 = float(input("Digite mais um número: "))

# Calcular a soma dos dois números:
soma = num1 + num2

# Exibe a soma dos dois números:
print("A soma dos dois números é: ", soma)


# Crie um programa que leia um número do usuário e exiba a sua raiz quadrada.
# Importando a biblioteca matemática:
import math

# Lê número do usuário:
numero = float(input("Digite um número: "))

# Calcular raiz quadrada do número:
raiz_quadrada = math.sqrt(numero)

# Exibe a raiz quadrada do número:
print("A raiz quadrada de ", numero, "é: ",raiz_quadrada)


# Crie um programa que leia uma palavra do usuário e exiba a primeira letra dessa palavra.
# Lê a palavra do usuário:
palavra = input("Digite uma palavra: ")

# Obter a primeira letra da palavra:
primeira_letra = palavra[0]

# Exibe a primera letra da palavra:
print("A primeira letra da palavra: ", palavra, "é: ", primeira_letra)


# Crie um programa que leia um número do usuário e determine se esse número é par ou ímpar.
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    
    print(numero, "É um número par!")
    
else:
    print(numero, "É um número ímpar!")


# Crie um programa que leia uma lista de números do usuário e exiba a soma desses números.
# Criar lista vazia
lista = []

# Ler os números e adicioná-los à lista
while True:
    numero = input("Digite um número (ou 's' para sair): ")
    if numero == 's':
        break
    # Colocar os numeros para float
    lista.append(float(numero))
  
# Calcular a soma dos números na lista
soma = sum(lista)
# Exibir a soma dos números
print("A soma dos números é: ", soma)

# Crie um programa que leia uma lista de palavras do usuário e exiba a palavra mais longa.

lista = []

# Ler as palavras e adicioná-las à lista
while True:
    palavra = input("Digite uma palavra (ou 's' para sair): ")
    if palavra == 's':
        break
    lista.append(palavra)
    
# Encontrar a palavra mais longa da lista
mais_longa = ""
for palavra in lista:
    if len(palavra) > len(mais_longa):
        mais_longa = palavra
        
        
# Exibe a palavra mais longa
print("A palavra mais longa é: ", mais_longa)


# Crie um programa que leia uma lista de números do usuário e exiba o maior número dessa lista.
numeros = input("Insira uma lista de números separados por vírgula: ")

# Converte a entrada em uma lista de números inteiros
numeros = [int(num) for num in numeros.split(",")]

# Encontra o maior número na lista usando a função max()
maior_numero = max(numeros)

# Exibe o maior número na lista
print("O maior número na lista é:", maior_numero)

# Crie um programa que leia uma lista de números do usuário e exiba o maior número dessa lista.
# Digitar os números
numeros = input("Digite uma sequência de números separados por espaço: ")

# Converter a sequêcia para lista e definir como float os números
numeros = [float(num) for num in numeros.split(" ")]

# Definir o menor número
menor_numero = min(numeros)

# Exibe menor número
print("O menor número da lista é: ",menor_numero)


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

# Crie um programa que leia uma lista de números do usuário e exiba somente os números pares.
numeros = input("Digite uma sequêcia de números separados por vírgula: ")
numeros = numeros.split(",")

print("Os números pares são: ")
for numero in numeros:
    if int(numero) % 2 == 0:
        print(numero)
        
        
# Crie um programa que leia uma lista de números do usuário e exiba somente os números ímpares
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = numeros.split(",")

print("Os números ímpares são: ")
for numero in numeros:
    if int(numero) % 2 != 0:
        print(numero)
        
        
# Crie um programa que leia uma lista de palavras do usuário e exiba somente as palavras que começam com a letra "a".
palavras = input("Digite uma lista de palavras, separadas por vírgula: ")
palavras = palavras.split(",")

print("As palavras que começão com a letra 'a' são: ")
for palavra in palavras:
    if palavra.lower().startswith('a'):
        print(palavra)
        
  
# Crie um programa que leia uma lista de números do usuário e exiba somente os números maiores do que 10.      
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = numeros.split(",")

print("Os números maiores que 10 são: ")
for numero in numeros:
    if int(numero) > 10:
        print(numero)
        
        
        
        
# Crie um programa que leia uma lista de números do usuário e exiba somente os números menores do que 5.
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = [int(num) for num in numeros.split(",")]  # converte a string em uma lista de inteiros

print("Números menores do que 5:")
for num in numeros:
    if num < 5:
        print(num)


# Crie um programa que leia uma lista de números do usuário e exiba a soma dos números pares.
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = [int(num) for num in numeros.split(",")]  # converte a string em uma lista de inteiros

soma_pares = 0
for num in numeros:
    if num % 2 == 0:  # verifica se o número é par
        soma_pares += num # inclementar os numeros e somá-los

print("A soma dos números pares é:", soma_pares)

# Crie um programa que leia uma lista de números do usuário e exiba a soma dos números ímpares.
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = [int(num) for num in numeros.split(",")]  # converte a string em uma lista de inteiros

soma_impares = 0
for num in numeros:
    if num % 2 != 0:  # verifica se o número é ímpar
        soma_impares += num # inclementar os numeros e somá-los

print("A soma dos números ímpares é:", soma_impares)


#Crie um programa que leia uma lista de números do usuário e exiba o produto desses números.
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = [int(num) for num in numeros.split(",")]  # converte a string em uma lista de inteiros

produto = 1
for num in numeros:
    produto *= num

print("O produto dos números é:", produto)



# Crie um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem crescente.
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = [int(num) for num in numeros.split(",")]  # converte a string em uma lista de inteiros

numeros.sort()  # ordena a lista em ordem crescente

print("A lista em ordem crescente é:", numeros)


# Crie um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem decrescente.
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = [int(num) for num in numeros.split(",")]  # converte a string em uma lista de inteiros

numeros.sort(reverse=True)  # ordena a lista em ordem decrescente

print("A lista em ordem decrescente é:", numeros)