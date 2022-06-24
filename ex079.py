'''Desenvolva um programa que leia 10 números inteiros e guarde-os em um vetor. No final, mostre quais são os números pares que foram digitados e em que posições eles estão armazenados.'''
lista = []
for i in range(2):
    num = int(input('Número: '))
    lista.append(num)
for i in lista:
    if i % 2 == 0:
        print(f'Par: {i}')
        print(f'Posição: {lista.index(i)}')