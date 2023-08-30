#0: Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
for i in range (1,51):#aqui um for onde o i que sera chamado depois, entra numa lista com numeros e pra isso que serve p range !
    if i % 2 !=0:# Dentro do loop, a condição if i % 2 != 0: verifica se o número i é ímpar. O operador % calcula o resto da divisão de i por 2. Se o resto for diferente de 0, significa que i é ímpar e o bloco de código dentro do if será executado.
        print (i)# pedindo para mostrar a variavel i...