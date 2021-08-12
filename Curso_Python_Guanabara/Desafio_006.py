"""
    Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
import time

print('\n')

time.sleep(1)
print('\033[1;32m*\033[m' * 50)
numero = int(input('\033[1;33mDigite um número inteiro: \033[m'))
print('\n')

time.sleep(1)
print('\033[1;33mNúmero Digitado:\033[m \033[1;31m[{}]\033[m'.format(numero))
print('\n')

time.sleep(1)
print('\033[1;33mDobro:\033[m \033[1;31m[{}]\033[m'.format(numero * 2))
print('\n')

time.sleep(1)
print('\033[1;33mTriplo:\033[m \033[1;31m[{}]\033[m'.format(numero * 3))
print('\n')

time.sleep(1)
print('\033[1;33mRaiz Quadrada:\033[m \033[1;31m[{}]\033[m'.format(numero ** (1/2)))
print('\033[1;32m*\033[m' * 50)

print('\n')


