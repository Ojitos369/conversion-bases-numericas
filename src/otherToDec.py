import math
def conversion(n,base):
    numerosCambio = [10,11,12,13,14,15]
    letras = 'ABCDEF'
    letrasCambio = ['A','B','C','D','E','F']
    n.reverse()
    resultado = 0
    for i in range(len(n)):
        aux = n[i]
        if n[i] in letras:
            for j in range(len(numerosCambio)):
                if n[i] == letrasCambio[j]:
                    aux = numerosCambio[j]
        resultado += int(aux)*(math.pow(base,i))
    return int(resultado)