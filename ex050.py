'''Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e
mostre na tela:
a) Quais foram os números sorteados
b) Quantos números estão acima de 5
c) Quantos números são divisíveis por 3'''
from random import randint
num = 1
numeros = []
maior = 0
divisivel = 0
while num <= 20:
    numero = randint(0, 10)
    numeros.append(numero)
    if numero > 5:
        maior += 1
    if numero % 3 == 0:
        divisivel += 1
    num += 1
print('Valores sorteados: ',end='')
print(*(numeros))
print(f'Desses valores, {maior} são maiores que 5 e {divisivel} são divisiveis por 3')