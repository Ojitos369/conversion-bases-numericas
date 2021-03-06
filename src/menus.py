from src.otherToDec import conversion
from src.extras import pausar, limpiar, convertir


def menuMain():
    inc = True
    while inc:
        limpiar()
        opc = input('''1.- Entrada decimal
2.- Entrada binaria
3.- Entrada Octal
4.- Entrada Hexadecimal
5.- Conversion Libre
6.- Configurar el numero de decimales
7.- Salir
Elige una opcion: ''')
        opc = convertir(opc)
        if opc > 0 and opc < 8:
            inc = False
        else:
            print('Opcion no valida. Intenta nuevamente')
            pausar()
    return opc

def numeroDecimal(text = 'Ingresa un numero: ', textError='Numero no valido'):
    valido = '0123456789.'
    inc = True
    n = 0
    while inc:
        limpiar()
        n = input(text)
        correcto = True
        #n = convertir(n)
        for i in range(len(n)):
            if n[i] in valido:
                pass
            else:
                correcto = False
                print(textError)
                pausar()
        if correcto: inc = False
    return n

def numero(valido,texto='Ingresa un numero: ', textError='Numero no valido'):
    inc = True
    n = 0
    while inc:
        correcto = True
        limpiar()
        n = input(texto)
        n = n.upper()
        for i in range(len(n)):
            if not (n[i] in valido):
                correcto = False
        if correcto:
            inc = False
        else:
            print(textError)
            pausar()
    return n

def general(textError='Numero no valido'):
    letras = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
    letrasCambio = letras.split(',')
    inc = True
    base = 0
    validas = '.'
    conversiones = []
    while inc:
        limpiar()
        opc = input('Ingresa la base original: ')
        opc = convertir(opc)
        if opc > 1:
            base = opc
            inc = False
        else:
            print(textError)
            pausar()
    inc = True
    while inc:
        limpiar()
        aux = True
        opc = input('Ingresa la(s) base(s) a convertir, ejemplo: 2,8,16,etc: ')
        opc = opc.replace(' ','')
        conversiones = opc.split(',')
        bucle = True
        for i in range(len(conversiones)):
            try:
                if not (int(conversiones[i]) > 1):
                    print('Al menos un numero no es valido. Vuelve a intentar')
                    pausar()
                    aux = False
                    break
            except:
                print('Al menos un numero no es valido. Vuelve a intentar')
                pausar()
                aux = False
                break
        if aux: inc = False
    for i in range(base):
        if i < 10:
            validas = f'{validas}{i}'
            print(f'menor de 10{i}')
        else:
            validas = f'{validas}{letrasCambio[i-10]}'
            print(f'mayor de 10{i}')
    n = 0
    if base == 10:
        n = numeroDecimal()
    else:
        n = numero(validas)
    return [n,base,conversiones]