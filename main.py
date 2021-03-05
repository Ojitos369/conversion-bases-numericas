from time import sleep
from src.extras import pausar, limpiar, convertir
from src.menus import menuMain as menu
from src.decimal import main as decimal
from src.general import main as convertir
import src.menus as menus

def main():
    mostrar = True
    while mostrar:
        opc = menu()
        if opc != 5:
            if opc == 1:
                n = menus.numeroDecimal()
                decimal(n,[2,8,16])
                pausar()
            elif opc == 2:
                n = menus.numeroBinario()
                convertir(n,2,[8,16])
                pausar()
            elif opc == 3:
                n = menus.numeroOctal()
                convertir(n,8,[2,16])
                pausar()
            elif opc == 4:
                n = menus.numeroHexadecimal()
                convertir(n,16,[2,8])
                pausar()
        else:
            print('Adios')
            sleep(.5)
            limpiar()
            mostrar = False

if __name__ == "__main__":
    main()