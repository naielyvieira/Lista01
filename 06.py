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