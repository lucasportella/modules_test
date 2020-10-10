def aumentar(numero):
    numero = numero + (numero * 0.1)
    return numero


def reduzir(numero):
    numero = numero - (numero * 0.13)
    return numero


def dobro(numero):
    return numero * 2


def metade(numero):
    return numero / 2


def moeda(numero,moeda='R$'):
    return f'{moeda}{numero:.2f}'.replace('.',',')

