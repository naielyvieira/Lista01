# Crie um programa que leia um número do usuário e determine se esse número é par ou ímpar.
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    
    print(numero, "É um número par!")
    
else:
    print(numero, "É um número ímpar!")