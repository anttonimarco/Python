"""
    Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""
import time

time.sleep(1)
print('\n')
print('\033[1;36m*\033[m' * 45)
print('\n')

time.sleep(1)
print('       \033[1;32m>>> Teacher Software <<<\033[m')
print('\n')

time.sleep(1)
nota_1 = float(input('\033[1;33mDigite a Primeira Nota: \033[m'))
print('\n')
time.sleep(1)
nota_2 = float(input('\033[1;33mDigite a Segunda Nota: \033[m'))

resultado = (nota_1 + nota_2) / 2
print('\n')

time.sleep(1)
print('\033[1;33mA Média entre P.N\033[m\033[1;31m[{}]\033[m \033[1;33me S.N\033[m\033[1;31m[{}]\033[m \033[31;33mé: M\033[m\033[1;31m[{}]\033[m'.format(nota_1, nota_2, resultado))
print('\n')

if resultado <= 4.99:
    time.sleep(1)
    print('        \033[1;31m>>> ALUNO REPROVADO! <<<\033[m')
else :
    time.sleep(1)
    print('        \033[1;34m>>> ALUNO APROVADO! <<<\033[m')

time.sleep(1)
print('\n')
print('\033[1;36m*\033[m' * 45)
