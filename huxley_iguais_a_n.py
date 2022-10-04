lista = []

for i in range(0,101,1):
        num = int(input())
        lista.append(num)

ultimo = lista[100]

for i in range (0,100,1):
        if(lista[i] == ultimo):
            print(i)