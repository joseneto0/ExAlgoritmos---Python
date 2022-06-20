#Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela. No final, analise a média e mostre se o aluno teve ou não um bom aproveitamento (se ficou acima da média 7.0).
nome = input('Digite seu nome: ')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Sua média é {media}')
if media >= 7:
    print('Você foi aprovado :)')
else:
    print('Você não foi aprovado :(')