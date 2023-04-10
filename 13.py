# Crie um programa que leia uma lista de palavras do usuário e exiba somente as palavras que começam com a letra "a".
palavras = input("Digite uma lista de palavras, separadas por vírgula: ")
palavras = palavras.split(",")

print("As palavras que começão com a letra 'a' são: ")
for palavra in palavras:
    if palavra.lower().startswith('a'):
        print(palavra)