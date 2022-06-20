#Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar.
from datetime import datetime
nascimento = int(input('Digite seu ano de nascimento: '))
idade = datetime.now().year - nascimento
print(f'Você tem {idade} anos')
if idade >= 18 and idade < 70:
    print('Voto Obrigatório!')
elif idade >= 16 or idade > 70:
    print('Voto não Obrigatório')
elif idade < 16:
    print('Não Vota')