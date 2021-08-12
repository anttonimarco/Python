"""
    Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
    primitivo e todas as informações possíveis sobre ele.
"""
import time

print('\n')
print('=' * 60)
print('<< Type Program >>')
print('\n')

dado = input('Digite qualquer dado para visualizar suas informações \n')
print('\n')

print('Tipo Primitivo')
print(type(dado))
print('\n')

print('É Alfabetico?')
print(dado.isalpha())
print('\n')

print('É Alfanumérico?')
print(dado.isalnum())
print('\n')

print('Só tem Espaços?')
print(dado.isspace())
print('\n')

print('Está em Maiúsculo?')
print(dado.isupper())
print('\n')

print('Está em Minúsculo?')
print(dado.islower())
print('\n')

print('Está Capitalizada?')
print(dado.istitle())
print('\n')


print('É um número?')
print(dado.isnumeric())
print('=' * 60)
print('\n')








