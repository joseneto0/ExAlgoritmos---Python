'''Faça um programa usando a estrutura “faça enquanto” que leia a idade de
várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou
não continuar a digitar dados. No final, quando o usuário decidir parar, mostre
na tela:
a) Quantas idades foram digitadas
b) Qual é a média entre as idades digitadas
c) Quantas pessoas tem 21 anos ou mais.'''
qntd = 0
soma = 0
maiores_21 = 0
while True:
    idade = int(input('Digite sua idade: '))
    qntd += 1
    soma += idade
    if idade >= 21:
        maiores_21 += 1
    continuar = input('Quer continuar? [S/N] ').upper()
    if continuar == 'N':
        break
print('=' * 20)
print(f'Foram digitadas {qntd} idades')
print(f'A média entre as idades digitadas é de {soma // qntd}')
print(f'{maiores_21} pessoa(s) tem 21 anos ou mais de idade')