n = int(input())

string = input()

lista = string.split()

novalista = list(map(int, lista))

menor_valor = novalista[0]
menor_index = 0 

for i in range(1,n,1):
        if(menor_valor > novalista[i]):
                menor_valor = novalista [i]
                menor_index = i

print("Menor valor:",menor_valor)
print("Posicao:",menor_index)