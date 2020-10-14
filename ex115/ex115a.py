from time import sleep
from ex115.modulos.cores import colorizar
flag = False
while flag == False:
    print('-'*60)
    print(f'{"MENU PRINCIPAL":^60}')
    print('-'*60)
    print(f'{colorizar("1","amarelo")} - {colorizar("Ver pessoas cadastradas","azul")}')
    print(f'{colorizar("2","amarelo")} - {colorizar("Cadastrar nova pessoa","azul")}')
    print(f'{colorizar("3","amarelo")} - {colorizar("Sair do sistema","azul")}')
    print('-'*60)
    try:
        opção = int(input(f'{colorizar("Sua opção: ","amarelo")}'))
        opção > 0
    except (TypeError, ValueError):
        print(f'{colorizar("ERRO: Digite um número inteiro válido!","vermelho")}')
        continue
    else:
         if opção < 1 or opção > 3:
             print(f'{colorizar("ERRO: Número digitado fora do intervalo!","vermelho")}')
             continue
         elif opção == 1:
             print('-' * 60)
             print(f'{f"Opção {opção}":^60}')
             print('-' * 60)
             sleep(2)
         elif opção == 2:
             print('-' * 60)
             print(f'{f"Opção {opção}":^60}')
             print('-' * 60)
             sleep(2)
         elif opção == 3:
             print('-' * 60)
             print(f'{f"Opção {opção}":^60}')
             print('-' * 60)
             sleep(2)
             print(f'{"Saindo do sistema... Até logo!":^60}')
             print('-' * 60)
             break