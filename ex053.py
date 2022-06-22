'''Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
a) Quantos homens foram cadastrados
b) Quantas mulheres foram cadastradas
c) A média de idade do grupo
d) A média de idade dos homens
e) Quantas mulheres tem mais de 20 anos'''
num = 1
homens = 0
mulheres = 0
soma_total = 0
soma_homens = 0
mulheres_20 = 0
while num <= 5:
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: [M/F] ').upper()
    while sexo not in 'MF':
        sexo = input('Tente Novamente. Digite seu sexo: [M/F] ').upper()
    if sexo == 'M':
        homens += 1
        soma_homens += idade
    elif sexo == 'F':
        mulheres += 1
        if idade > 20:
            mulheres_20 += 1
    soma_total += idade
    num += 1
print(f'Foram cadastrados {homens} homens e {mulheres} mulheres')
print(f'A média de idade do grupo foi de {soma_total // 5} anos e a média de idade dos homens foi de {soma_homens // homens} anos')
print(f'{mulheres_20} mulheres tem mais de 20 anos de idade')