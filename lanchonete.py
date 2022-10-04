#Uma lanchonete está com preços promocionais em seu cardápio.
#  A condição é que uma pessoa só pode escolher um item da lista, porém, 
# a quantidade deste item é ilimitada, o cliente pode comprar quantos quiser.
#  De acordo com o cardápio abaixo, elabore um programa que receba o código do item escolhido e 
# a quantidade que o cliente irá comprar. Em seguida, calcule e apresente o valor da conta a pagar. 
# Caso um código inexistente seja informado o usuário deverá receber uma mensagem de erro. 
# A quantidade de itens só deverá ser solicitada se o usuário informar um código válido. 
# Caso o usuário informe 0 a aplicação deve parar
#cachorro quente - 2.50
#x-tudo - 4.75
#batata frita - 3.25
#refrigerante - 2.80
#pipoca - 0.90

total = 0
while True:
        order = int(input())
        if order == 0:
                print('Código inválido')
                break
        amount = int(input(""))
        if order == 1:
                order = 'Cachorro Quente'
                total = 2.50 * amount
                print('Você escolheu', order)
        elif order == 2:
                order = 'X-Tudo'
                total = 4.75 * amount
                print('Você escolheu', order)
        elif order == 3:
                order = 'Batata frita'
                total = 3.25 * amount
                print('Você escolheu', order)
        elif order == 4:
                order = 'Refrigerante'
                total = 2.80 * amount
                print('Você escolheu', order)
        elif order == 5:
                order = 'Pipoca'
                total = 0.90 * amount
                print('Você escolheu', order)
        print(f'Sua conta é de R${total}')
