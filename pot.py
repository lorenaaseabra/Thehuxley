def potenciacao_em_lista(lista):
    lista_2=[]
    if len(lista)==0:
        return lista
    if len(lista)==1:
        return lista
    lista_2.append(lista[0])
    for num in range(1,len(lista)-1):
        if lista[num] %2==0:
            lista_2.append(lista[num]**2)
        if lista[num] %2!=0:
            lista_2.append(lista[num]**3)
    lista_2.append(lista[-1])
    return lista_2

lista = eval(input())
resultado = potenciacao_em_lista(lista)
print(resultado)