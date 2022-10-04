num = -1 

multiplicador = int(input())
resp = 0
for i in range (-1, 10):
        num = num + 1
        resp = num*multiplicador
        #print dentro do loop
        print('{} x {} = {}'.format(num, multiplicador, resp))