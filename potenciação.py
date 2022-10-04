#Escreva a função potenciacao_em_lista(lista) que recebe uma lista de números inteiros por parâmetro. 
# A função deve retornar (devolver) uma lista de mesmo tamanho que a lista recebida por parâmetro, 
# na qual os elementos pares devem ser elevados ao quadrado e os elementos ímpares elevados ao cubo,
#  com exceção do primeiro e do último elemento (os de índice 0 e len(lista)-1), 
# que deverão ser mantidos intactos.
#OBS: preste bastante atenção aos casos especiais quando a lista for vazia ou tiver um único elemento
#  (neste último caso, os índices de início e fim são iguais, então o valor deve ser mantido intacto).


# Escreva a funcao potenciacao_em_lista(lista) abaixo:
#Insira o código aqui



def potenciacao_em_lista(lista):
        list(lista)
        for i in range (1, len(lista)-1):
                if lista[i] % 2 == 0: 
                        lista[i] = lista[i]**2
                if lista[i] % 2 != 0:
                        lista[i] = lista[i]**3        
        return lista
# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
lista = eval(input()) 
resultado = potenciacao_em_lista(lista)
print(resultado)