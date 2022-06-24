'''Crie um programa que preencha automaticamente um vetor numérico com 7 números gerados aleatoriamente pelo computador e depois mostre os valores gerados na tela'''
from random import randint
lista = []
for i in range(7):
    lista.append(randint(0, 10))
print(lista)