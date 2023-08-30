#-1: Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
#caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido!

while True: #quando verdade
    nota = float(input("Digite uma nota de zero a dez!")) #fez uma váriável onde pede pro usuario digitar a nota
    if nota < 0 or nota > 10:# se a variavel for menor que 0 ou maior que 10
        print("Valor inválido! A nota deve estar entre 0 e 10!")# vai receber uma mensagem dizendo que a nota deve ser entre 0 e 10

    else: # senão 
        break # para o programa ...

print("nota válida:", nota)#receberá um print dizendo que a nota é válida!  

# Exercício feito com ajuda porém, entendi as linhas e não lembrava ao bem commo começar...