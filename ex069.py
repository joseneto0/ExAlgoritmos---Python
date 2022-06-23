'''[DESAFIO] Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética), mostrando na tela os 10 primeiros elementos da PA e a soma entre todos os valores da sequência.'''
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
ultimo = primeiro + (10 - 1) * razao
ultimo += 1
soma = 0
for i in range(primeiro, ultimo, razao):
    print(i, end=' ')
print('FIM!')