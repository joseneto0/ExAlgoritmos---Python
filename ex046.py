#Crie um programa que calcule e mostre na tela o resultado da soma entre 6 + 8 + 10 + 12 + 14 + ... + 98 + 100.
num = 6
soma = 0
while num <= 100:
    soma += num
    print(num, end=' ')
    num += 2
print('Acabou!')
print(f'Soma dos valores: {soma}')