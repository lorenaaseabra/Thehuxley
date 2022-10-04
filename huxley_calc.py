n1 = float(input())
flag = 0
operacao = 'x'
resultado = 0

while(operacao != "&"):
        n2 = float(input())
        operacao = input()
        if(operacao != "&"):
                if(operacao == "+"):
                        if(flag ==0):
                                resultado = n1 + n2
                                print(f'{resultado:.3f}')
                        else:
                                resultado = resultado + n2
                                print(f'{resultado:.3f}')
                elif(operacao == "-"):
                        if(flag ==0):
                                resultado = n1 - n2
                                print(f'{resultado:.3f}')
                        else:
                                resultado = resultado - n2
                                print(f'{resultado:.3f}')
                elif(operacao == "*"):
                        if(flag ==0):
                                resultado = n1 * n2
                                print(f'{resultado:.3f}')
                        else:
                                resultado = resultado * n2
                                print(f'{resultado:.3f}')
                elif(operacao == "/"):
                        if(flag ==0):
                                resultado = n1 / n2
                                print(f'{resultado:.3f}')
                        elif n2 == 0:
                                print("operacao nao pode ser realizada")
                        else:
                                resultado = resultado / n2
                                print(f'{resultado:.3f}')
        flag += 1