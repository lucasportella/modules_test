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
        arquivo = open(nome,'wt+')
        arquivo.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
      nome = open(nome,'r')
      print(nome.read())
    except:
        print('Erro ao ler arquivo!')
def cadastrarPessoaNoArquivo(nome, pessoa):
    nome = open(nome)