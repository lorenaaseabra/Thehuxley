index = 0 
password = {}
letras = []

string = input()

stringminuscula = string.lower()
string1 = stringminuscula.title()
stringline = string1.replace("\n","")
stringa = stringline.replace("a","@")
stringE = stringa.replace("E","%")
stringe = stringE.replace("e","!")
stringi = stringe.replace("i","@")
stringo = stringi.replace("o","#")
stringu = stringo.replace("u","$")
stringspace = stringu.replace(" ","")

quantity = int(input())

for i in range(quantity+1):
        numeromagico = int(input())
        while numeromagico <= 5:
                numeromagico = int(input())
        senha = f"{stringspace[index:index+5]}{stringspace[-5:]}{stringspace[numeromagico:numeromagico+5]}"
        
        for letra in senha:
                letras.append(letra)
        letras.reverse()
        senha ="".join(letras)
        letras = []
        print(senha)
        
        resposta = input()
        if resposta == 's':
                user = input()
                password[user] = senha 
                index += 1
print(password)


