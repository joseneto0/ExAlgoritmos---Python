'''Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
a) Qual é a média de idade do grupo
b) Quantas pessoas tem mais de 18 anos
c) Quantas pessoas tem menos de 5 anos
d) Qual foi a maior idade lida'''
num = 1
soma = 0
maior_18 = 0
menor = 0
maior_idade = 0
while num <= 10:
    valores = int(input('Digite a idade: '))
    soma += valores
    if valores > maior_idade:
        maior_idade = valores
    if valores > 18:
        maior_18 += 1
    elif valores < 5:
        menor += 1
    num += 1
print(f'A média de idade do grupo é: {soma // 10} anos')
print(f'{maior_18} pessoas tem mais de 18 anos')
print(f'{menor} pessoas tem menos de 5 anos')
print(f'{maior_idade} foi a maior idade lida')