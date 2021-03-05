#from src.extras import pausar, limpiar, convertir

def conversion(original, cambio):
    numerosCambio = [10,11,12,13,14,15]
    letrasCambio = ['A','B','C','D','E','F']
    continuar = True
    resultados = []
    aux = original
    while continuar:
        residuo = int(aux%cambio)
        aux -= residuo
        aux /= cambio
        if residuo > 9:
            for i in range(len(numerosCambio)):
                if residuo == numerosCambio[i]:
                    residuo = letrasCambio[i]
        resultados.append(residuo)
        if aux == 0:
            continuar = False
    resultados.reverse()
    return resultados