#from src.extras import pausar
#import math

def conversion(original, cambio,numDecimales):
    cambio = int(cambio)
    numerosCambio = []
    for i in range(26):
        numerosCambio.append(i+10)
    letras = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
    letrasCambio = letras.split(',')
    continuar = True
    resultados = []
    decimales = float(original)%1
    aux = int(float(original)-decimales)
    while continuar:
        residuo = int(aux%cambio)
        aux -= residuo
        aux /= cambio
        if residuo > 9:
            for i in range(len(numerosCambio)):
                if residuo == numerosCambio[i]:
                    residuo = letrasCambio[i]
        if not (residuo == 0 and aux == 0):
            resultados.append(residuo)
        if aux == 0:
            continuar = False
    resultados.reverse()
    
    if decimales > 0:
        resultados.append('.')
        for i in range(numDecimales):
            aux2 = decimales * cambio
            frac = int(aux2)
            decimales = aux2-frac
            if frac > 9:
                for j in range(len(numerosCambio)):
                    if frac == numerosCambio[j]:
                        frac = letrasCambio[j]
            resultados.append(frac)
            if decimales == 0:
                break
            
    return resultados