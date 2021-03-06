#from src.menus import numero
#from src.extras import pausar, limpiar, convertir
from src.decToOther import conversion

def main(n,cambios,decimales):
    print()
    for i in range(len(cambios)):
        numero = conversion(n,cambios[i],decimales)
        for j in range(len(numero)):
            print(f'{numero[j]}',end='')
        print(f' base {cambios[i]}\n')