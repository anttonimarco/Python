"""
    Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 
    5 % de desconto.
"""
import time

print('\n')
print('\033[1;36m\6 \033[m' * 30)

print('\033[1;35m               >>> Cadastro de Produtos <<<\033[m')
print('\n')

identidade = int(input('\033[1;33mDigite um ID para o produto: \033[m'))
nome_produto = input('\033[1;33mDigite o nome do produto: \033[m')
preco_produto = float(input('\033[1;33mQual o preço original do produto? R$ \033[m'))
desconto = preco_produto - (preco_produto * 5/100)
print('\n')

time.sleep(1)
print('\033[1;33mID do Produto: \033[m{}'.format(identidade))
time.sleep(1)
print('\033[1;33mNome do Produto: \033[m{}'.format(nome_produto.capitalize()))
time.sleep(1)
print('\033[1;33mPreço Original R$ \033[m{:.2f}'.format(preco_produto))
time.sleep(1)
print('\033[1;33mPreço com Desconto de 5% R$ \033[m{:.2f}'.format(desconto))
time.sleep(1)

print('\033[1;36m\6 \033[m' * 30)
print('\n')


