"""
    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
    desse ângulo.

"""
from math import radians, sin, cos, tan # De biblioteca math importe radians, sin, cos, tan.
import time # Importando time.

print('\b') # Pula linha.

print('\033[1;31m=\033[m' * 45) # Separador.
print('        \033[1;33m>>> Seno Cosseno Tangente <<<\033[m') # Título Script.
print('\033[1;31m=\033[m' * 45)

angulo = float(input('\033[1;32mDigite o ângulo que você deseja: \033[m')) # Variável angulo recebe dados tipo float.
seno = sin(radians(angulo)) # Variável seno recebe o resultado.

time.sleep(1)   # Intervalo entre as exibicções.
print('\b')
print('\033[1;32mO ângulo de \033[m\033[1;33m{}\033[m \033[1;32mtem o SENO de\033[m \033[1;33m{:.2f}\033[m'.format(angulo, seno)) # Exibindo na tela. 
cosseno = cos(radians(angulo)) # Variável cosseno recebe o resultado.

time.sleep(1)   # Intervalo entre as exibicções.
print('\b')
print('\033[1;32mO ângulo de\033[m \033[1;33m{}\033[m \033[1;32mtem o COSSENO de \033[m\033[1;33m{:.2f}\033[m'.format(angulo, cosseno)) # Exibindo na tela.
tangente = tan(radians(angulo)) # Variável tangente recebe o resultado.

time.sleep(1)   # Intervalo entre as exibicções.
print('\b')
print('\033[1;32mO ângulo de \033[m\033[1;33m{}\033[m \033[1;32mtem a TANGENTE de\033[m \033[1;33m{:.2f}\033[m'.format(angulo, tangente)) # Exibindo na tela.
print('\033[1;31m=\033[m' * 45)

print('\b')