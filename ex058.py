'''Faça um algoritmo que leia a idade de vários alunos de uma turma. O programa
vai parar quando for digitada a idade 999. No final, mostre quantos alunos
existem na turma e qual é a média de idade do grupo.'''
soma = 0
qntd = 0
idade = int(input('Digite sua idade: '))
while idade != 999:
    soma += idade
    qntd += 1
    idade = int(input('Digite sua idade: '))
media = soma / qntd
print(f'Total de alunos da turma: {qntd}')
print(f'Média da turma: {media}')