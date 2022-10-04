#Escreva um programa que receba um texto em uma única linha e 
#imprima cada caractere e o número de vezes que ocorre no texto, na ordem inversa à alfabética.

caracter = input()
lista = list(caracter)
dicto = {}

for object in lista:
        occurrences = lista.count(object)
        d = {object:occurrences}  
        dicto.update(d)

for i in reversed(sorted(dicto)):
        print(i,dicto[i])
