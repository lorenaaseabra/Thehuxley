#A partir dessa lista ela pensou em montar um programa que, colocado um nome N e um presente P,
#o programa retorna se a pessoa acertou ou não no presente para seu amigo secreto.
#Só que Jocelina não sabe muito de programação, e acabou precisando de ajuda para montar esse programa. 
#Você, sendo tomado(a) pelo espírito natalino, aceitou o desafio!
#A entrada consiste em diversos casos de teste e termina com a string FIM. 
#A primeira linha contém um número X (3 ≤ X ≤ 20) que representa a quantidade de participantes no amigo secreto.
#Em seguida, as próximas X linhas irão conter o nome N e as 3 opções de presentes desejados P. 
#Em seguida, as próximas linhas irão conter um nome N e um presente P, 
#representando as consultas realizadas no programa.
quantity = int(input())
pessoa = {}
lista_dict = []

for i in range(0,quantity,1): 
                string = input().split()
                pessoa = {
                        string[0] : [string[1],string[2],string[3]]
                }
                lista_dict.append(pessoa)

nome_pesquisa = ""
while(nome_pesquisa != "FIM"):
        lista_pesquisa = input().split()
        if(len(lista_pesquisa) > 1):
                nome_pesquisa = lista_pesquisa[0]
                pres_pesquisa = lista_pesquisa[1]
                flag = 0
                for elem in lista_dict:
                        keys = list(elem.keys())
                        values = list(elem.values())
                        if(keys[0] == nome_pesquisa and pres_pesquisa in values[0]):
                                flag = 1
                                break
                if(flag == 1):
                        print("Uhul! Seu amigo secreto vai adorar")
                else:
                        print("Tente Novamente!")
        else:
                nome_pesquisa = lista_pesquisa[0]

       