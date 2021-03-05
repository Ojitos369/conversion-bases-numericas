from src.extras import pausar, limpiar, convertir


def menuMain():
    inc = True
    while inc:
        limpiar()
        opc = input('''1.- Entrada decimal
2.- Entrada binaria
3.- Entrada Octal
4.- Entrada Hexadecimal
5.- Salir
Elige una opcion: ''')
        opc = convertir(opc)
        if opc > 0 and opc < 6:
            inc = False
        else:
            print('Opcion no valida. Intenta nuevamente')
            pausar()
    return opc

def numeroDecimal(text = 'Ingresa un numero: ', textError='Numero no valido'):
    inc = True
    n = 0
    while inc:
        limpiar()
        n = input(text)
        n = convertir(n)
        if n > 0 or n < 0:
            inc = False
        else:
            print(textError)
            pausar()
    return n

def numeroBinario(text = 'Ingresa un numero Binario: ', textError='Numero no valido'):
    valido = '01'
    inc = True
    n = 0
    while inc:
        correcto = True
        limpiar()
        n = input(text)
        for i in range(len(n)):
            if not (n[i] in valido):
                correcto = False
        if correcto:
            inc = False
        else:
            print(textError)
            pausar()
    return list(n)

def numeroOctal(text = 'Ingresa un numero base 8: ', textError='Numero no valido'):
    valido = '012345678'
    inc = True
    n = 0
    while inc:
        correcto = True
        limpiar()
        n = input(text)
        for i in range(len(n)):
            if not (n[i] in valido):
                correcto = False
        if correcto:
            inc = False
        else:
            print(textError)
            pausar()
    return list(n)

def numeroHexadecimal(text = 'Ingresa un numero base 16: ', textError='Numero no valido'):
    valido = 'ABCDEF0123456789'
    inc = True
    n = 0
    while inc:
        correcto = True
        limpiar()
        n = input(text)
        n = n.upper()
        for i in range(len(n)):
            if not (n[i] in valido):
                correcto = False
        if correcto:
            inc = False
        else:
            print(textError)
            pausar()
    return list(n)