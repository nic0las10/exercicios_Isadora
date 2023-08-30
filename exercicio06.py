#6: Faça um Programa que leia cinco números e mostre o maior e o menor deles.

#Inicializando as variaveis com valores exrtremos

maior = float('-inf')
menor = float('inf')

#loop para ler os numeros 

for i in range(5):
    numero = float(input(f"digite o {i +1}° número:"))
    
    #Atualizando o maior e o menor número
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero 

# exibindo o resultado


print(f"O maior número é :{[maior]}")
print(f" O menor número é: {menor} ")

