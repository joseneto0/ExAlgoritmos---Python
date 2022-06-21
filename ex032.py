#[DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o jogador vai tentar descobrir qual foi o valor sorteado.
from random import randint
print('=' * 20)
print('ADVINHE O NÚMERO'.center(20))
print('=' * 20)
num = int(input('Digite um número: [1-5] '))
pc = randint(1, 5)
if num == pc:
    print('Você achou o número :D')
else:
    print('Você errou o número :C')
    print(f'O pc sorteou o número {pc}')