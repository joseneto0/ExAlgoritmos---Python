'''Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
na tela uma das mensagens abaixo:
- O primeiro valor é o maior
- O segundo valor é o maior
- Não existe valor maior, os dois são iguais'''
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    print(f'O primeiro número {num1} é o maior')
elif num2 > num1:
    print(f'O segundo número {num2} é o maior')
else:
    print('Os dois números são iguais')
