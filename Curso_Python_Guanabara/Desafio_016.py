"""
    Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
EX:
    Digite um número: 6.127 O número 6.127 tem a parte Inteira 6.
"""
print('\n')

print('-' * 45)
print('              >>> REAL <<<')
print('\n')
numero = float(input('Digite um valor: '))
print('\n')

print('A parte inteira do número {} é {}'.format(numero, int(numero)))
print('-' * 45)
print('\n')