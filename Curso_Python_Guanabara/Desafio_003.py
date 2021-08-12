"""
    Crie um programa que leia dois números e mostre a soma entre eles.
"""
import time


print('\n')
print('\033[1;32m=\033[m' * 50)
print('\033[1;36m<< Calculadora Soma >>\033[m')
print('\n')
numero_1 = int(input('\033[1;33mDigite um número:\033[m '))
time.sleep(1)
print('\n')
numero_2 = int(input('\033[1;33mDigite outro número:\033[m '))
time.sleep(1)
print('\n')
resultado = (numero_1 + numero_2)
print('\033[1;33mO resultado da soma entre\033[m \033[1;34m[{}]\033[m \033[1;33me\033[m \033[1;34m[{}]\033[m \033[1;33mé:\033[m \033[1;31m[{}]\033[m'.format(numero_1, numero_2, resultado))
print('\033[1;32m=\033[m' * 50)
print('\n')