from ex115ag.lib.interface import *
from ex115ag.lib.cores import colorizar
from time import sleep
while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print(colorizar('ERRO! Digite uma opção válida','vermelho'))
    sleep(2)