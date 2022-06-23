'''Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas.
O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
a) O nome da pessoa mais velha
b) O nome da mulher mais jovem
c) A média de idade do grupo
d) Quantos homens tem mais de 30 anos
e) Quantas mulheres tem menos de 18 anos'''
nome_velho = ''
mulher_jovem = ''
menor_idade = 0
soma = 0
qntd = 0
maior = 0
qntd_30 = 0
qntd_18 = 0
while True:
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: [M/F] ').upper()
    continuar = input('Quer continuar? [S/N] ').upper()
    if idade > maior:
        maior = idade
        nome_velho = nome
    if sexo == 'M':
        if idade > 30:
            qntd_30 += 1
    elif sexo == 'F':
        if idade < 18:
            qntd_18 += 1
        if qntd == 0:
            menor_idade = idade
            mulher_jovem = nome
        if idade < menor_idade:
            menor_idade = idade
            mulher_jovem = nome
        qntd += 1
    soma += idade
    if continuar == 'N':
        break
print('=' * 30)
print(f'Nome da pessoa mais velha: {nome_velho}')
print(f'Nome da mulher mais jovem: {mulher_jovem}')
print(f'Média de idade do grupo: {soma // qntd}')
print(f'{qntd_30} homens tem mais de 30 anos')
print(f'{qntd_18} mulheres tem menos de 18 anos')