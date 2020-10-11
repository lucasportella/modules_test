def aumentar(numero,percentual, formatar=True):
    '''
    :param numero: número que foi inserido para fazer o cálculo
    :param percentual: porcentagem do aumento
    :param formatar: se True vai formatar para o padrão brasileiro, False fica original do python
    :return: retorna o número com formatação ou sem formatação
    '''
    numero = numero + (numero * (percentual/100))
    if formatar == False:
        return numero
    else:
        return moeda(numero)


def reduzir(numero,percentual=13,formatar=True):
    numero = numero - (numero * (percentual/100))
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
    return f'{moeda} {numero:.2f}'.replace('.',',')


def resumo(valor, aumento_porcento=10, redução_porcento=10):
    '''
    :param valor: valor escolhido pelo usuário
    :param aumento_porcento: percentual de aumento
    :param redução_porcento: percentual de redução
    :return:
    '''

    print('-' * 40)
    print(f"{'RESUMO DO VALOR':^40}")
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor)}')
    print(f'Metade do preço: \t{metade(valor)}')
    print(f'{aumento_porcento}% de aumento: \t{aumentar(valor,aumento_porcento)}')
    print(f'{redução_porcento}% de redução: \t{reduzir(valor,redução_porcento)}')
    print('-' * 40)
