'''Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai
perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:
a) qual é a maior idade lida
b) quantos homens foram cadastrados
c) qual é a idade da mulher mais jovem
d) qual é a média de idade entre os homens'''
soma = 0
maior = 0
homens = 0
mulher_jovem = 0
cont_f = 0
while True:
    sexo = input('Digite seu sexo: [M/F] ').upper()
    idade = int(input('Digite sua idade: '))
    continuar = input('Quer continuar? [S/N] ').upper()
    if idade > maior:
        maior = idade
    if sexo == 'M':
        homens += 1
        soma += idade
    elif sexo == 'F':
        if cont_f == 0:
            mulher_jovem = idade
        elif idade < mulher_jovem:
            mulher_jovem = idade
        cont_f += 1
    if continuar == 'N':
        break
print(f'Maior idade lida: {maior}')
print(f'Homens cadastrados: {homens}')
print(f'Idade da mulher mais jovem: {mulher_jovem}')
if homens != 0:
    print(f'Média de idade dos homens: {soma // homens}')
else:
    print(f'Média das idades dos homens: {soma}')