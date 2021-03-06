from src.otherToDec import conversion
from src.decimal import main as decimal

def main(n,base,conversiones,decimales):
    aux=list(n)
    print()
    for i in range(len(aux)):
        print(f'{aux[i]}',end='')
    print(f' base {base}')
    numero = conversion(n,base,decimales)
    decimal(numero,conversiones,decimales)