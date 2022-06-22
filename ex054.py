'''Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando
no final:
a) Qual foi a média de altura do grupo
b) Quantas pessoas pesam mais de 90Kg
c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.'''
num = 1
soma_altura = 0
mais_90 = 0
menos_50 = 0
mais_100 = 0
while num <= 7:
    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    soma_altura += altura
    if peso > 90:
        mais_90 += 1
    elif peso < 50 and altura < 1.60:
        menos_50 += 1
    if peso > 100 and altura > 1.90:
        mais_100 += 1
    num += 1
print(f'A média de altura do grupo é de: {soma_altura / 7:.2f}m')
print(f'{mais_90} pessoas pesam mais de 90kg')
print(f'{menos_50} pessoas pesam menos de 50kg e tem a altura menor que 1.60m')
print(f'{mais_100} pessoas tem mais de 100kg e tem a altura maior que 1.90m')
