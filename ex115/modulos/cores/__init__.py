def colorizar(texto_para_colorir,cor_escolhida):
    if cor_escolhida == 'vermelho':
        texto_para_colorir = f'\033[0;31m{texto_para_colorir}\033[m'
    elif cor_escolhida == 'verde':
        texto_para_colorir = f'\033[0;32m{texto_para_colorir}\033[m'
    elif cor_escolhida == 'amarelo':
        texto_para_colorir = f'\033[0;33m{texto_para_colorir}\033[m'
    elif cor_escolhida == 'azul':
        texto_para_colorir = f'\033[0;34m{texto_para_colorir}\033[m'
    return texto_para_colorir