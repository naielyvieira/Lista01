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