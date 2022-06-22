#Desenvolva um programa que mostre na tela a seguinte contagem: 100 95 90 85 80 ... 0 Acabou!
num = 100
while num >= 0:
    print(num, end=' ')
    num -= 5
print('Acabou!')