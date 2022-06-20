'''Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
situação em relação ao alistamento militar.
 - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o
alistamento.
 - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do
alistamento.'''
from datetime import datetime
ano = int(input('Ano de nascimento: '))
idade = datetime.now().year - ano
print(f'Você tem {idade} anos')
if idade < 18:
    print(f'Faltam {18 - idade} ano para o alistamento')
elif idade == 18:
    print('Você está no ano do alistamento :D')
else:
    print(f'Já passou {idade - 18} ano(s) do alistamento')

