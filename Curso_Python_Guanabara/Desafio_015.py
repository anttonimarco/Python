"""
    Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a 
    quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
    custa R$60 por dia e R$0,15 por KM rodado.
"""
import time

print('\n')

print('\033[1;36m=\033[m' * 60)
print('\033[1;35m                      >>> Loca Car <<<\033[m')
print('\n')

quant_dias = int(input('\033[1;33mDigite quantos dias o carro permaneceu alugado: \033[m'))
km_percorr = int(input('\033[1;33mDigite a quantidade de KM percorridos: \033[m'))
print('\n')

result_dias = quant_dias * 60
result_km = km_percorr * 0.15
totalpagar = (result_dias + result_km)

time.sleep(1)
print('\033[1;33mValor pelos\033[m \033[1;31m{}\033[m \033[1;33mdias alugado R$\033[m\033[1;31m{:.2f}\033[m'.format(quant_dias, result_dias))
time.sleep(1)
print('\033[1;33mValor pelos\033[m \033[1;31m{}\033[m \033[1;33mkms rodados R$\033[m\033[1;31m{:.2f}\033[m'.format(km_percorr, result_km))

print('\n')
time.sleep(1)
print('\033[1;33mTotal a pagar R$\033[m\033[1;31m{:.2f}\033[m'.format(totalpagar))

time.sleep(1)
print('\033[1;36m=\033[m' * 60)
