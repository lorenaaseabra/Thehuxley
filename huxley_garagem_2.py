entrada = input()

entrada = list(map(int, entrada.split()))

if(entrada[0] >= entrada[3] and entrada[1] >= entrada[4] and entrada[2] >= entrada[5]):
        print("SIM\n")
else:
        print('NAO\n')        
