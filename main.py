from time import sleep
from src.extras import pausar, limpiar, convertir
from src.menus import menuMain as menu
from src.decimal import main as decimal
from src.general import main as conversion
import src.menus as menus

def main():
    mostrar = True
    while mostrar:
        opc = menu()
        if opc != 6:
            if opc == 1:
                n = menus.numero('0123456789.',10)
                conversion(n,10,[2,8,16])
                pausar()
            elif opc == 2:
                n = menus.numero('01.',2)
                conversion(n,2,[8,16])
                pausar()
            elif opc == 3:
                n = menus.numero('012345678.',8)
                conversion(n,8,[2,16])
                pausar()
            elif opc == 4:
                n = menus.numero('ABCDEF0123456789.',16)
                conversion(n,16,[2,8])
                pausar()
            elif opc == 5:
                n,base,conversiones = menus.general()
                if int(base) == 10:
                    decimal(n,conversiones)
                else: 
                    conversion(n,base,conversiones)
                pausar()
        else:
            print('Adios')
            sleep(.5)
            limpiar()
            mostrar = False

if __name__ == "__main__":
    main()