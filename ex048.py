#Faça um programa que leia 7 números inteiros e no final mostre o somatório entre eles.
num = 1
soma = 0
while num <= 7:
    valor = int(input('Digite um valor: '))
    soma += valor
    num += 1
print(f'A soma dos valores é: {soma}')