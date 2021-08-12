"""
    Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
"""
import time

print('\n')
print('\033[1;35m=\033[m' * 25) 
name = input(' \033[1;32mOlá, qual é o seu nome?\033[m \n')
print('\n')
time.sleep(1)
print(' \033[1;33mSeja Bem-Vindo \033[1;32m{}\033[m\033[1;33m!\033[m\033[m'.format(name.capitalize()))
print('\033[1;35m=\033[m' * 25)
print('\n')
