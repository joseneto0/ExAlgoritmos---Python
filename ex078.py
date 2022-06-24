'''Escreva um programa que leia 15 números e guarde-os em um vetor. No final, mostre o vetor inteiro na tela e em seguida mostre em que posições foram digitados valores que são múltiplos de 10.'''
lista = []
for i in range(3):
    num = int(input('Número: '))
    lista.append(num)
print(lista)
for i in lista:
    if i % 10 == 0:
        print(lista.index(i), end=' ')