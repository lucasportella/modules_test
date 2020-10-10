from ex109 import moeda
preço = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço)}')
print(f'Aumentado em 10%, temos {moeda.aumentar(preço)}')
print(f'Reduzindo em 13%, temos {moeda.reduzir(preço)}')
