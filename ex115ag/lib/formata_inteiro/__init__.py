from ex115ag.lib.cores import colorizar
def leiaEscolha(escolha):
    while True:
        try:
            escolha = int(input(colorizar(escolha,'verde')))
        except (ValueError,TypeError):
            print(f'{colorizar("ERRO: por favor, digite um número inteiro válido.","vermelho")}')
            continue
        except (KeyboardInterrupt):
            print(f'{colorizar("Usuário preferiu não digitar esse número","vermelho")}.')
            return 0
        else:
            return escolha
