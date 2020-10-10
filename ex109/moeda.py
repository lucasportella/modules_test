def aumentar(numero,formatar=True):
    '''

    :param numero: número que foi inserido para fazer o cálculo
    :param formatar: se True vai formatar para o padrão brasileiro, False fica original do python
    :return: retorna o número com formatação ou sem formatação
    '''
    numero = numero + (numero * 0.1)
    if formatar == False:
        return numero
    else:
        return moeda(numero)


def reduzir(numero,formatar=True):
    numero = numero - (numero * 0.13)
    if formatar == False:
        return numero
    else:
        return moeda(numero)


def dobro(numero,formatar=True):
    if formatar == False:
        return numero * 2
    else:
        return moeda(numero * 2)


def metade(numero,formatar=True):
    if formatar == False:
        return numero / 2
    else:
        return moeda(numero/2)

def moeda(numero,moeda='R$'):
    return f'{moeda}{numero:.2f}'.replace('.',',')

