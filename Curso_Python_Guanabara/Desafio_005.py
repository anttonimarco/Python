"""
    Faça um programa que leia um número inteiro e mostre na tela o seu antecessor
e seu sucessor.
"""
import time

print('\n')
time.sleep(1)
print("\033[1;36m*\033[m" * 70)
print('\n')
time.sleep(1)
print('                \033[1;32m>>> Antecessor & Sucessor Program <<<\033[m')
print('\n')
time.sleep(1)
numero_inteiro = int(input('\033[1;33mDigite um número inteiro: \033[m'))
print('\n')
time.sleep(1)
print('\033[1;33mNúmero Digitado: \033[m \033[1;31m[{}]\033[m'.format(numero_inteiro))
print('\n')
time.sleep(1)
print('\033[1;33mAntecessor: \033[m \033[1;31m[{}]\033[m'.format(numero_inteiro -1))
print('\n')
time.sleep(1)
print('\033[1;33mSucessor: \033[m \033[1;31m[{}]\033[m'.format(numero_inteiro + 1))
print('\n')
time.sleep(1)
print("\033[1;36m*\033[m" * 70)