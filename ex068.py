'''Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura “para”. No final, mostre na tela:
a) Quantas mulheres foram cadastradas
b) Quantos homens pesam mais de 100Kg
c) A média de peso entre as mulheres
d) O maior peso entre os homens'''
mulheres = 0
homens_100 = 0
soma_mulheres = 0
maior_homens = 0
qntd_mulheres = 0
for i in range(8):
    sexo = input('Digite seu sexo: [M/F] ').upper()
    peso = float(input('Digite seu peso: '))
    if sexo == 'F':
        mulheres += 1
        soma_mulheres += peso
        qntd_mulheres += 1
    elif sexo == 'M':
        if peso > maior_homens:
            maior_homens = peso
        if peso > 100:
            homens_100 += 1
print('=' * 20)
print(f'Foram cadastradas {mulheres} mulheres')
print(f'{homens_100} homens pesam mais de 100kg')
print(f'A média do peso das mulheres ficou de {soma_mulheres / qntd_mulheres}kg')
print(f'O maior peso entre os homens foi de {maior_homens}kg')