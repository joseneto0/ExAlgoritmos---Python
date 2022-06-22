'''Faça um algoritmo que pergunte ao usuário um número inteiro e positivo
qualquer e mostre uma contagem até esse valor:
Ex: Digite um valor: 35
Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!'''
contador = 1
num = int(input('Digite um número inteiro positivo: '))
while num < 0:
    num = int(input('Tente Novamente. Digite um número inteiro positivo: '))
while contador <= num:
    print(contador, end=' ')
    contador += 1
print('Acabou!')