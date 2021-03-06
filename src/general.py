from src.otherToDec import conversion
from src.decimal import main as decimal

def main(n,base,conversiones):
    n=list(n)
    print()
    for i in range(len(n)):
        print(f'{n[i]}',end='')
    print(f' base {base}')
    numero = conversion(n,base)
    decimal(numero,conversiones)