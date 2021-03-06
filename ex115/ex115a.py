from time import sleep
from ex115.modulos.cores import colorizar
from ex115.modulos.menu_principal import menu_principal
from ex115.modulos.bloco import formatar_opção
from ex115.modulos.arquivo import arquivoExiste, criarArquivo, lerArquivo, cadastrarPessoaNoArquivo

arquivo = 'cadastroRegistro.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    menu_principal()
    try:
        opção = int(input(f'{colorizar("Sua opção: ","amarelo")}'))
    except (TypeError, ValueError):
        print(f'{colorizar("ERRO: Digite um número inteiro válido!","vermelho")}')
        sleep(1)
        continue
    else:
         if opção < 1 or opção > 3:
             print(f'{colorizar("ERRO: Número digitado fora do intervalo!","vermelho")}')
             sleep(1)
             continue
         elif opção == 1:
            formatar_opção("OPÇÃO 1 - VER CADASTRADOS")
            lerArquivo(arquivo)
         elif opção == 2:
             formatar_opção("OPÇÃO 2 - NOVO CADASTRO")
             cadastrarPessoaNoArquivo(arquivo)
         elif opção == 3:
             formatar_opção("OPÇÃO 3 - SAIR DO SISTEMA")
             print(f'{"Saindo do sistema... Até logo!":^60}')
             print('-' * 60)
             break