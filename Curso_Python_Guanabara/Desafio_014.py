"""
    Escreva um programa que converta uma temperatura digitada em °C e converta para ºF
"""

print('\n')

print('\033[1;36m=\033[m' * 40)

print('\033[1;31m          >>> Cel for Fah <<<\033[m')
print('\n')

celcius = float(input('\033[1;33mDigite a temperatura em Celcius: \033[m'))

fahrenheit = (celcius * 9/5) + 32

print('\n')

print('\033[1;33mTemperatura Digitada \nCelcius: \033[m\033[1;31m{}°\033[m'.format(celcius))
print('\n')

print('\033[1;33mTemperatura Convertida \nFahrenehit: \033[m\033[1;31m{}°\033[m'.format(fahrenheit))

print('\033[1;36m=\033[m' * 40)
print('\n')