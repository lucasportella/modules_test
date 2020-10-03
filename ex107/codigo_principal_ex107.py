from ex107 import alterar_preço
preço = float(input('Digite o preço: R$'))
print(f'A metade de {preço} é {alterar_preço.metade(preço):.2f}')
print(f'O dobro de {preço} é {alterar_preço.dobro(preço):.2f}')
print(f'Aumentado em 10%, temos {alterar_preço.aumentar(preço):.2f}')
print(f'Reduzindo em 13%, temos {alterar_preço.reduzir(preço):.2f}')