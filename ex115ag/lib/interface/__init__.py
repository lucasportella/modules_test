from ex115ag.lib.formata_inteiro import leiaEscolha
from ex115ag.lib.cores import colorizar

def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{colorizar(c,"amarelo")} - {colorizar(item,"azul")}')
        c += 1
    print(linha())
    opc = leiaEscolha('Sua opção: ')
    return opc