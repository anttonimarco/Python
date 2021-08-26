"""
    Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
import random
import time

on = True

while on == True:
    print('\b')
    print('=' * 40)
    print('            >>> Sorteio <<<')
    print('=' * 40)

    print('[2] Sorteio entre Dois')
    print('[3] Sorteio entre Três')
    print('[4] Sorteio entre Quatro')
    print('[5] Sorteio entre Cinco')
    print('[0] Sair')
    print('\b')
    choice = int(input('Digite o número de sua escolha: '))

    if choice == 2:
        print('\b')
        name_1 = input('Primero nome: ')
        name_2 = input('Segundo nome: ')
        sorteio_dedois = random.randint(1, 3)
        if sorteio_dedois == 1:
            time.sleep(1)
            print('\nO Aluno(a) sorteado foi: {}\n'.format(name_1.capitalize()))
            time.sleep(1)
            print('Parabéns {}! Uruulll!\n'.format(name_1.capitalize()))
            time.sleep(1)
            sorteio_dedois = 0
            choiceExit = input('Aperte enter para continuar...')
            
        elif sorteio_dedois == 2:
            time.sleep(1)
            print('\nO Aluno(a) sorteado foi: {}\n'.format(name_2.capitalize()))
            time.sleep(1)
            print('Parabéns {}! Uruulll!\n'.format(name_2.capitalize()))
            time.sleep(1)
            sorteio_dedois = 0
            choiceExit = input('Aperte enter para continuar...')
            
    elif choice == 3:
        print('\b')
        name_3 = input('Primeiro nome: ')
        name_4 = input('Segundo  nome: ')   
        name_5 = input('Trceiro  nome: ')
        sorteio_detres = random.randint(1,4)
        if sorteio_detres == 1:
            time.sleep(1)
            print('\nO Aluno(a) sorteado foi: {}\n'.format(name_3.capitalize()))
            time.sleep(1)
            print('Parabéns {}! Uruulll!\n'.format(name_3.capitalize()))
            time.sleep(1)
            sorteio_detres = 0
            choiceExit = input('Digite qualquer tecla para continuar...')
            
        elif sorteio_detres == 2:
            time.sleep(1)
            print('\nO Aluno(a) sorteado foi: {}\n'.format(name_4.capitalize()))
            time.sleep(1)
            print('Parabéns {}! Uruulll!\n'.format(name_4.capitalize()))
            time.sleep(1)
            sorteio_detres = 0
            choiceExit = input('Digite qualquer tecla para retornar...')
            
        elif sorteio_detres == 3:
            time.sleep(1)
            print('\nO Aluno(a) sorteado foi: {}\n'.format(name_5.capitalize()))
            time.sleep(1)
            print('Parabéns {}! Uruulll!\n'.format(name_5.capitalize()))
            time.sleep(1)
            sorteio_detres = 0
            choiceExit = input('Digite qualquer tecla para retornar...')

    elif choice == 4:
        print('\b')
        name_6 = input('Primeiro nome: ')
        name_7 = input('Segundo  nome: ')
        name_8 = input('Terceiro nome: ')
        name_9 = input('Quarto   nome: ')
        sorteio_dequatro = random.randint(1,5)
       
        if sorteio_dequatro == 1:
            time.sleep(1)
            print('\nO Aluno(a) sorteado foi: {}\n'.format(name_6.capitalize()))
            time.sleep(1)
            print('Parabéns {}! Uruulll!\n'.format(name_6.capitalize()))
            time.sleep(1)
            sorteio_dequatro = 0
            choiceExit = input('Digite qualquer tecla para continuar...')
       
        elif sorteio_dequatro == 2:
            time.sleep(1)
            print('\nO Aluno(a) sorteado foi: {}\n'.format(name_7.capitalize()))
            time.sleep(1)
            print('Parabéns {}! Uruulll!\n'.format(name_7.capitalize()))
            time.sleep(1)
            sorteio_dequatro = 0
            choiceExit = input('Digite qualquer tecla para retornar...')
        
        elif sorteio_dequatro == 3:
            time.sleep(1)
            print('\nO Aluno(a) sorteado foi: {}\n'.format(name_8.capitalize()))
            time.sleep(1)
            print('Parabéns {}! Uruulll!\n'.format(name_8.capitalize()))
            time.sleep(1)
            sorteio_dequatro = 0
            choiceExit = input('Digite qualquer tecla para retornar...')
        
        elif sorteio_dequatro == 4:
            time.sleep(1)
            print('\nO Aluno(a) sorteado foi: {}\n'.format(name_9.capitalize()))
            time.sleep(1)
            print('Parabéns {}! Uruulll!\n'.format(name_9.capitalize()))
            time.sleep(1)
            sorteio_dequatro = 0
            choiceExit = input('Digite qualquer tecla para retornar...')

    elif choice == 5:
        print('\b')
        name_10 = input('Primeiro nome: ')
        name_11 = input('Segundo  nome: ')
        name_12 = input('Terceiro nome: ')
        name_13 = input('Quarto   nome: ')
        name_14 = input('Quinto   nome: ')
        sorteio_decinco = random.randint(1,6)
      
        if sorteio_decinco == 1:
            time.sleep(1)
            print('\nO Aluno(a) sorteado foi: {}\n'.format(name_10.capitalize()))
            time.sleep(1)
            print('Parabéns {}! Uruulll!\n'.format(name_10.capitalize()))
            time.sleep(1)
            sorteio_decinco = 0 
            choiceExit = input('Digite qualquer tecla para continuar...')
       
        elif sorteio_decinco == 2:
            time.sleep(1)
            print('\nO Aluno(a) sorteado foi: {}\n'.format(name_11.capitalize()))
            time.sleep(1)
            print('Parabéns {}! Uruulll!\n'.format(name_11.capitalize()))
            time.sleep(1)
            sorteio_decinco = 0
            choiceExit = input('Digite qualquer tecla para retornar...')
        
        elif sorteio_decinco == 3:
            time.sleep(1)
            print('\nO Aluno(a) sorteado foi: {}\n'.format(name_12.capitalize()))
            time.sleep(1)
            print('Parabéns {}! Uruulll!\n'.format(name_12.capitalize()))
            time.sleep(1)
            sorteio_decinco = 0
            choiceExit = input('Digite qualquer tecla para retornar...')
        
        elif sorteio_decinco == 4:
            time.sleep(1)
            print('\nO Aluno(a) sorteado foi: {}\n'.format(name_13.capitalize()))
            time.sleep(1)
            print('Parabéns {}! Uruulll!\n'.format(name_13.capitalize()))
            time.sleep(1)
            sorteio_decinco = 0
            choiceExit = input('Digite qualquer tecla para retornar...')
        
        elif sorteio_decinco == 5:
            time.sleep(1)
            print('\nO Aluno(a) sorteado foi: {}\n'.format(name_14.capitalize()))
            time.sleep(1)
            print('Parabéns {}! Uruulll!\n'.format(name_14.capitalize()))
            time.sleep(1)
            sorteio_decinco = 0
            choiceExit = input('Digite qualquer tecla para retornar...')

    elif choice == 0:
        print('\b')
        print('Saindo em 3')
        time.sleep(1)
        print('Saindo em 2')
        time.sleep(1)
        print('Saindo em 1')
        time.sleep(1)
        on = False
        
        
        
 

