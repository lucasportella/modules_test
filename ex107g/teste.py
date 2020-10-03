from ex107g import moeda
preço = float(input('Digite o preço: R$'))
print(f'A metade de {preço} é {moeda.metade(preço):.2f}')
print(f'O dobro de {preço} é {moeda.dobro(preço):.2f}')
print(f'Aumentado em 10%, temos {moeda.aumentar(preço):.2f}')
print(f'Reduzindo em 13%, temos {moeda.reduzir(preço):.2f}')