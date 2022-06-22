#Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 + 450 + 400 + 350 + 300 + ... + 50 + 0
num = 500
soma = 0
while num >= 0:
    soma += num
    print(num, end=' ')
    num -= 50
print('Acabou!')
print(f'Soma dos valores: {soma}')