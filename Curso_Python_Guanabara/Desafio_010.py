"""
    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
    quantos Dólares ela pode comprar. Considere US$1,00 = R$4,70
"""

print('\n')

print('\033[1;31m*\033[m' * 50)
print('\033[1;36m               >>> Convert Money <<<\033[m')
print('\033[1;31m*\033[m' * 50)

print('\n')
reais = float(input('\033[1;33mQuantos reais você tem na carteira?\nR$: \033[m'))
dolar = 4.75

print('\n')
print('\033[1;33mCom\033[m \033[1;36mR${:.2f}\033[m \033[1;33mvocê consegue comprar \033[m\033[1;36mUS${:.2f}\033[m'.format(reais, (reais / dolar)))
print('\n')

print('\033[1;31m*\033[m' * 50)



