#from src.extras import pausar, limpiar, convertir

def conversion(original, cambio):
    numerosCambio = []
    for i in range(26):
        numerosCambio.append(i+10)
    letras = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
    letrasCambio = letras.split(',')
    continuar = True
    resultados = []
    aux = original
    while continuar:
        residuo = int(int(aux)%int(cambio))
        aux -= int(residuo)
        aux /= int(cambio)
        if residuo > 9:
            for i in range(len(numerosCambio)):
                if residuo == numerosCambio[i]:
                    residuo = letrasCambio[i]
        if not (residuo == 0 and aux == 0):
            resultados.append(residuo)
        if aux == 0:
            continuar = False
    resultados.reverse()
    return resultados