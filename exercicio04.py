#4: Faça um programa que, dado um conjunto de N números, determine o menor valor, o
#maior valor e a soma dos valores

#Solicita o numero de elementos no conjunto
n = int(input("Dígite o numero do elemento no conjunto:"))

#Inicializa as váriaveis para armazenar o menor, o maior e a soma dos valores
 
menor = float('inf')
maior = float('-inf')
soma = 0

#loop para ler os números e calcular o menor, o maior e a soma...

for i in range(n):
    num = float(input(f"Digite o elemento {i+1}:  "))
    menor = min(menor,num)
    maior = max(maior,num)
    soma += num

#imprime os resultados  
print(f"o menor valor é : {menor}")
print(f"o maior vallor é: {maior}")
print (f"a soma dos valores é {soma}")   

#Pode se usar esse exemplo para as notas de um aluno!
# ex. 10 provas a menor, a maior e á média! 


