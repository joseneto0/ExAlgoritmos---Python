'''Crie um programa usando a estrutura “faça enquanto” que leia vários números.
A cada laço, pergunte se o usuário quer continuar ou não. No final, mostre na
tela:
a) O somatório entre todos os valores
b) Qual foi o menor valor digitado
c) A média entre todos os valores
d) Quantos valores são pares'''
soma = 0
menor = 0
pares = 0
qntd = 0
while True:
    numeros = int(input('Digite um número: '))
    if qntd == 0:
        menor = numeros
    elif numeros < menor:
        menor = numeros
    soma += numeros
    if numeros % 2 == 0:
        pares += 1
    qntd += 1
    continuar = input('Deseja continuar? [S/N] ').upper()
    if continuar == 'N':
        break
print('=' * 20)
print(f'O somatório de todos os valores é de {soma}')
print(f'O menor valor digitado foi o {menor}')
print(f'A média dos valores foi de {soma // qntd}')
print(f'{pares} números são pares')