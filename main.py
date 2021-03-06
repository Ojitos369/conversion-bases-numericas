from time import sleep
from src.extras import pausar, limpiar, convertir
from src.menus import menuMain as menu
from src.decimal import main as decimal
from src.general import main as conversion
import src.menus as menus

def main():
    decimales=5
    mostrar = True
    while mostrar:
        opc = menu()
        if opc != 7:
            if opc == 1:
                n = menus.numero('0123456789.')
                conversion(n,10,[2,8,16],decimales)
                pausar()
            elif opc == 2:
                n = menus.numero('01.')
                conversion(n,2,[10,8,16],decimales)
                pausar()
            elif opc == 3:
                n = menus.numero('012345678.')
                conversion(n,8,[10,2,16],decimales)
                pausar()
            elif opc == 4:
                n = menus.numero('ABCDEF0123456789.')
                conversion(n,16,[10,2,8],decimales)
                pausar()
            elif opc == 5:
                n,base,conversiones = menus.general()
                conversion(n,base,conversiones,decimales)
                pausar()
            elif opc == 6:
                decimales = menus.numero('0123456789','Ingresa el numero de decimales. Por defecto 5: ')
                decimales = int(decimales)

        else:
            print('Adios')
            sleep(.5)
            limpiar()
            mostrar = False

if __name__ == "__main__":
    main()