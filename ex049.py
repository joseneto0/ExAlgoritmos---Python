#Crie um programa que leia 6 números inteiros e no final mostre quantos deles são pares e quantos são ímpares.
num = 1
pares = 0
impares = 0
while num <= 6:
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1
    num += 1
print(f'No total, foram encontrados {pares} números pares e {impares} números impares')