"""
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
    retângulo, calcule e mostre o comprimento da hipotenusa.
"""

import math

print('\n')
print('\033[1;31m=\033[m' * 48)
print('             \033[1;36m >>> Math <<<\033[m')
print('\n')

ca = float(input('\033[1;33mDigite o comprimento do cateto adjacente: \033[m'))
co = float(input('\033[1;33mDigite o comprimento do cateto oposto: \033[m'))
print('\n')
hi = math.hypot(co, ca) 

print('\033[1;33mA hipotenusa vai medir {:.2f}\033[m'.format(hi))
print('\033[1;31m=\033[m' * 48)
print('\n')

