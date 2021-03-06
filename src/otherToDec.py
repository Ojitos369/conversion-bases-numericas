import math
def conversion(n,base):
    numerosCambio = []
    for i in range(26):
        numerosCambio.append(i+10)
    letras = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
    letrasCambio = letras.split(',')
    n.reverse()
    resultado = 0
    #print(numerosCambio)
    for i in range(len(n)):
        aux = n[i]
        if n[i] in letras:
            for j in range(len(numerosCambio)):
                if n[i] == letrasCambio[j]:
                    #print(numerosCambio[j])
                    aux = numerosCambio[j]
        #print(f'aux: {aux}, base: {base}, i: {i}')
        resultado += int(aux)*(math.pow(base,i))
    return int(resultado)