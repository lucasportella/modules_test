from ex115.modulos.cores import colorizar
def menu_principal():
    print('-' * 60)
    print(f'{"MENU PRINCIPAL":^60}')
    print('-' * 60)
    print(f'{colorizar("1", "amarelo")} - {colorizar("Ver pessoas cadastradas", "azul")}')
    print(f'{colorizar("2", "amarelo")} - {colorizar("Cadastrar nova pessoa", "azul")}')
    print(f'{colorizar("3", "amarelo")} - {colorizar("Sair do sistema", "azul")}')
    print('-' * 60)