# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num
#vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a
#7.0.

def calcular_media(notas):
    return sum(notas) / len (notas) # esta funçao definiu que sera tirado a media das notas... 


def main(): # main pelo que eu entendi é o nome padrão dado a dunção principal...
    num_alunos = 10# variavel com o numero de alunos
    notas_alunos = []#variavel com a nota dos alunos

    for i in range(num_alunos):#pesquisado-> range é utilizada para gerar uma sequência numérica dentro de um intervalo determinado. Ela é normalmente utilizada como auxiliar da função for. Em Python, podemos repetir uma ação por um número específico de vezes usando um “loop forcom” a função range
        # i seria uma "variavel inteira que swra usada "
        #chamou como parametro principa (num_alunos) variavel ja criada...
        notas =[]# variavel indicando uma lista de notas
        for j in range(4):# mesma coisa só que indicando numero da quantidade de notas pra se fazer a media 
            nota = float(input(f"Digite a nota {j +1} do aluno {i+1}: "))# variavel pedindo pro usuario digitar o numero das 4 notas em sequencias ate o aluno 10
        
            notas.append(nota)#é um recurso em Python que permite adicionar um elemento ao final de uma lista existente. Essa função é extremamete útil quando você precisa expandir uma lista com mais itens dinamicamente, sem precisar criar uma nova lista a cada vez.
            # eu entendi que ele ta juntando a lista "notas" com o que está no imput da variavel #nota#
        media = calcular_media(notas) # variavel indicando a funçao media da variavel notas
        notas_alunos.append(media)  # nota dos alunos em lista chamando a media feita a cima

    num_alunos_acima_7 = 0# Criada uma variavel pra dar "inicio" ...
    for media in notas_alunos: # para media da nota dos alunos
        if media >=7: # se media dor = ou maior que 7
            num_alunos_acima_7 += 1# EXPLICAR A LINHA DE RACIOCINIO

    print(f"Número de alunos com média maior ou igual a 7:{num_alunos_acima_7}")# pedindo atravéz de um print o numero de alunos com a media igual ou maior que 7               
    

if __name__ =="__main__":#  EXPLICAR A LINHA 
    main()# EXPLICAR A LINHA 
