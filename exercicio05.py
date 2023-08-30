#5: Faça um programa que calcule e mostre a média aritmética de N notas.
#N notas = o usuário pode selecionar a quantidade de notas

"""n = int(input("Dígite a quantidade de notas para calcular a média aritmética: "))


menor = float('inf')
maior = float('-inf')
media = 0

for i in range(n):
    num = float(input(f"Dígite a nota {i+1}"))
    menor = min (menor, num)
    maior = max (maior, num)
    soma = sum(i)
    quantidade = len(i) 
    media = soma / quantidade


print = (f" A Média das notas é: {media}") # Até aqui tente sozinho e depois fui consultar ..."""

#fotma correta do programa

#solicita o numeri de notas 
n = int(input("Dígite o numero de notas: "))
#inicializa a variavel para armazenar a soma das notas
soma_notas = 0 
#loop para ler as notas 
for i in range (n):
    nota = float(input(f"Dígite a nota {i+1}:"))
    soma_notas += nota

# Calcula a média     
media = soma_notas / n 

# Imprime o resultado
print (f"A média das notas é : {media}!")







