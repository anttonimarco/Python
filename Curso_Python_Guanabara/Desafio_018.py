"""
    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
    desse ângulo

"""
from math import radians, sin, cos, tan 
print('\b')

print('=' * 45)

ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print('\b')
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))

print('\b')
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))

print('\b')
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))
print('=' * 45)

print('\b')


