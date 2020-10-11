def leiaDinheiro(dinheiro):
    verificador = False
    while verificador == False:
        formatar_numero = input(dinheiro).strip()
        formatar_numero_real = formatar_numero
        quant_de_pontos = 0
        quant_de_virgulas = 0
        for c in formatar_numero_real:
            if c == '.':
                quant_de_pontos += 1
            if c == ',':
                quant_de_virgulas += 1

        formatar_numero = formatar_numero.replace('.','').replace(',','')

        if formatar_numero.isnumeric() == False or quant_de_pontos > 1 or quant_de_virgulas >1 or quant_de_virgulas + quant_de_pontos > 1:
            print("ERRO: O preço digitado não é válido!")
        else:
            if ',' in formatar_numero_real:
               formatar_numero_real = formatar_numero_real.replace(',','.')
            formatar_numero_real = float(formatar_numero_real)
            verificador = True

    return formatar_numero_real

