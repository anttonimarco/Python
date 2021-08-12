"""
    Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
    primitivo e todas as informações possíveis sobre ele.
"""
import time

print('\n')
time.sleep(1)
print('\033[1;36m*\033[m' * 60)
time.sleep(1)
print('\033[1;43m\033[3;30m<<< Type Program >>>\033[m\033[m')
print('\n')

time.sleep(1)
dado = input('\033[1;33mDigite algo:\033[m ')
print('\n')

time.sleep(1)
print('\033[1;33mTipo Primitivo\033[m')
print(type(dado))
print('\n')

time.sleep(1)
print('\033[1;33mÉ um número?\033[m')
print(dado.isnumeric())
print('\n')

time.sleep(1)
print('\033[1;33mÉ Alfabetico?\033[m')
print(dado.isalpha())
print('\n')

time.sleep(1)
print('\033[1;33mÉ Alfanumérico?\033[m')
print(dado.isalnum())
print('\n')

time.sleep(1)
print('\033[1;33mSó tem Espaços?\033[m')
print(dado.isspace())
print('\n')

time.sleep(1)
print('\033[1;33mEstá em Maiúsculo?\033[m')
print(dado.isupper())
print('\n')

time.sleep(1)
print('\033[1;33mEstá em Minúsculo?\033[m')
print(dado.islower())
print('\n')

time.sleep(1)
print('\033[1;33mEstá Capitalizada?\033[m')
print(dado.istitle())
print('\n')


time.sleep(1)
print('\033[1;36m*\033[m' * 60)
print('\n')








