'''[DESAFIO] Faça um programa que mostre os 10 primeiros elementos da Sequência de Fibonacci:
1 1 2 3 5 8 13 21...'''
n1 = 1
n2 = 1
print(n1, n2, end=' ')
for i in range(2, 10):
    fibo = n2 + n1
    n2 = n1
    n1 = fibo
    print(fibo, end=' ')
print('FIM!')