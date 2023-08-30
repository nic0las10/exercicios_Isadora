# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas
#seguido do seu comprimento. Informe também se as duas strings possuem o mesmo
#comprimento e são iguais ou diferentes no conteúdo.
#Compare duas strings
#String 1: Brasil Hexa 2022
#String 2: Brasil! Hexa 2022!

#Função para comparar e exibir resultados

def comparar_strings(string1, string2):
    print(f"string1:: {string1}")
    print(f"string 2: {string2}")

    len1 = len(string1)
    len2 = len(string2)

    print(f"Comprimento da string1:{len1}")
    print(f"Comprimento da string1:{len2}")

    if len1 == len2:
        print("As duas strings tem o mesmo cumprimento!")
    else:
        print("As duas strings tem cumprimento diferente!")

    if string1 == string2:
        print(" As duas strings são do mesmo conteudo!")
    else:
        print("As strings tem conteudos diferentes!")

# Lendo as duas strings

string1 = input("Digite a primeira string:")
string2 = input("Digite a segunda string:")

#chamando a função para comparar e exibir resultados 

comparar_strings(string1, string2)