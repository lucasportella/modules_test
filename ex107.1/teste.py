from moeda import metade, dobro, aumentar, reduzir
preço = float(input('Digite o preço: R$'))
print(f'A metade de {preço} é {metade(preço):.2f}')
print(f'O dobro de {preço} é {dobro(preço):.2f}')
print(f'Aumentado em 10%, temos {aumentar(preço):.2f}')
print(f'Reduzindo em 13%, temos {reduzir(preço):.2f}')