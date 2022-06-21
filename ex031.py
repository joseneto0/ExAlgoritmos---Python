#[DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)
from time import sleep
import random
nomes = ['PEDRA', 'PAPEL', 'TESOURA']
print('=' * 20)
print('JOKENPO'.center(20))
print('=' * 20)
print('''[1] - PEDRA
[2] - PAPEL
[3] - TESOURA''')
num = int(input('Qual sua opção? '))
num -= 1
print(f'Sua jogada {nomes[num]}')
sleep(0.7)
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO!!!!!')
pc = random.randint(0,2)
print(f'Jogada do pc: {nomes[pc]}')
if num == pc:
    print('Deu empate :O')
elif num == 0 and pc != 1:
    print('Você ganhou :D')
elif num == 1 and pc != 2:
    print('Você ganhou :D')
elif num == 2 and pc != 0:
    print('Você ganhou :D')
else:
    print('PC ganhou :C')