"""
    Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a 
quantidade de tinta necessário para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""
import time

print('\n')
print('\033[1;31m*\033[m' * 70)
print('\033[1;33m                          >>> Pintura <<<\033[m')
print('\033[1;31m*\033[m' * 70)
print('\n')

largura = float(input('\033[1;33mDigite a Largura da Parede: \033[m'))
print('\n')
altura = float(input('\033[1;33mDigite a Altura da Parede: \033[m'))
print('\n')

area = (largura * altura)
litros_tinta = (area / 2)

time.sleep(1)
print('\033[1;33mÁrea Total: \033 \033[1;41m{:.0f}\033[m \033[1;33mm²\033[m'.format(area))
print('\n')

time.sleep(1)
print('\033[1;33mLargura Digitada: \033 \033[1;41m{:.0f}\033[m \033[1;33mMetros\033[m'.format(largura))
print('\n')

time.sleep(1)
print('\033[1;33mAltura Digitada: \033 \033[1;41m{:.0f}\033[m \033[1;33mMetros\033[m'.format(altura))
print('\n')

time.sleep(1)
print('\033[1;33mLitros de tinta necessário para pintar está parede: \033[1;41m {:.0f}\033[m \033[1;33mLitros\033[m'.format(litros_tinta))
print('\n')

time.sleep(1)
print('\033[1;31m*\033[m' * 70)
print('\n')

