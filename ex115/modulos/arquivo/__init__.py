from time import sleep
from ex115.modulos.verificador import leiaInt
from ex115.modulos.bloco import formatar_opção
from ex115.modulos.cores import colorizar


def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        nome = open(nome, 'rt')
        formatar_opção('PESSOAS CADASTRADAS')
        for linha in nome:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{colorizar(dado[0], "roxo"):.<30}{colorizar(dado[1], "ciano"):<12} {colorizar("anos", "ciano")}')
        sleep(2)
    except:
        print('Erro ao ler arquivo!')


def cadastrarPessoaNoArquivo(nome):
    nome = open(nome, 'at')
    pessoa = str(input('Nome: '))
    idade = leiaInt('Idade: ')
    try:
        nome.write(f'{pessoa};{idade}\n')
    except:
        print('ERRO ao escrever os dados!')
    finally:
        print(f'Novo registro de {pessoa} adicionado com sucesso.')
        nome.close()
        sleep(2)
