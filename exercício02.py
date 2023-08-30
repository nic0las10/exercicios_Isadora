#-2: Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um
#crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma
#classificação sobre a participação da pessoa no crime. Se a pessoa
#responder positivamente a 2 questões ela deve ser classificada como
#"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
#contrário, ele será classificado como "Inocente".


perguntas_assassinato = [#criando uma variavél como lista citando as perguntas!
    "Telefonou para a vitima?",
    "Esteve no local do crime?",
    "Mora perto da Vitima?",
    "Devia para a vitima?",
    "Ja trabalhou com a vitima?"
]

respostas_positivas = 0#Pelo que eu entendí se da essa variavél para dar um inicio ou melhor dizendo um valor de onde se partir...

for pergunta in  perguntas_assassinato:#criado o for 
    resposta = input(pergunta+"(sim/não):")# variavel dizendo pra o usuario digitar o for ou seja as respostas da lista se é sim ou nao!
    if resposta.lower()== "sim":# lower é um método pra converter todos os caracteres da string em minusculas!
        respostas_positivas += 1# Não entendi bem a funcionalidade 

if respostas_positivas == 2:#se respostas do usuário for equivakente a duas vai receber o print dizendo que é suspeito...
    print("Suspeita!")
elif 3 <= respostas_positivas <= 4:# se for 3 e 4 vai receber o print dizendoque é cumplice...( achei que se usaria "or" mas é "e"...
    print("Cúmplice!")
elif respostas_positivas == 5:#se receber 5 respostas como sim vai ser considerado assassino!
    print("Assassino!")
else:
    print("Inocente!")    # se for uma ou zero é inocente!

#exercicio também feito com auxiolio mas entendi a logica e anotei nas linhas ....
# feito o teste    



