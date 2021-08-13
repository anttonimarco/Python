"""
    Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

import time

print('\n')
print('\033[1;36m*\033[m' * 45)
time.sleep(1)
print('\033[1;32m         >>> Distance Software <<<\033[m')
print('\n')

time.sleep(1)
metros = float(input('\033[1;33mDigite uma distância em Metros: \033[m'))
print('\n')

time.sleep(1)
print('\033[1;33mMetros Digitados:\033[m \033[1;31m[{}]\033[m \033[1;33mMetros\033[m'.format(metros))
print('\n')

time.sleep(1)
print('\033[1;32m         >>> Em {} Metros Temos <<<\033[m'.format(metros))
print('\n')

time.sleep(1)
print('\033[1;33mCentímetros:\033[m \033[1;31m[{:.0f}]\033[m \033[1;33mcm\033[m'.format(metros*100))
print('\n')

time.sleep(1)
print('\033[1;33mMilímetros:\033[m \033[1;31m[{:.0f}]\033[m \033[1;33mml\033[m'.format(metros*1000))

time.sleep(1)
print('\033[1;36m*\033[m' * 45)

