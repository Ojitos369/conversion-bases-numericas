import math
def conversion(n,base,decimales):
    numerosCambio = []
    fraccionarios = False
    for i in range(26):
        numerosCambio.append(i+10)
    letras = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
    letrasCambio = letras.split(',')
    if '.' in n:
        dividido = n.split('.')
        n = (dividido[0])
        fraccionarios = list(dividido[1])
    n = list(n)
    n.reverse()
    resultado = 0
    for i in range(len(n)):
        aux = n[i]
        if n[i] in letras:
            for j in range(len(numerosCambio)):
                if n[i] == letrasCambio[j]:
                    aux = numerosCambio[j]
        resultado += int(aux)*(math.pow(base,i))
    if fraccionarios:
        resultado = float(resultado)
        noDecimales = len(fraccionarios)
        if noDecimales > decimales: noDecimales = decimales
        for i in range(noDecimales):
            aux = fraccionarios[i]
            if fraccionarios[i] in letras:
                for j in range(len(numerosCambio)):
                    if fraccionarios[i] == letrasCambio[j]:
                        aux = numerosCambio[j]
            resultado += float(float(aux)*(math.pow(base,-(i+1))))
    return resultado