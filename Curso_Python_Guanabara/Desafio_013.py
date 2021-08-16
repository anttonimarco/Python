"""
    Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
    salário, com 15% de aumento.
"""

print('\n')
print('\033[1;36m\6 \033[m' * 20)
print('\033[1;35m       >>> Aumento de Salário <<<\033[m')
print('\n')

salario_original = float(input('\033[1;33mDigite o salário atual do funcionário \nR$ \033[m'))

print('\n')
aumento = salario_original + (salario_original * 15/100)


print('\033[1;33mSalário com aumento de 15% \nR$\033[m\033[1;31m {:.2f}\033[m'.format(aumento))

print('\033[1;36m\6 \033[m' * 20)

print('\n')

