#[DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32. A partir de agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4 tentativas para tentar acertar.
from random import randint
print('=' * 20)
print('ADVINHE O NÚMERO'.center(20))
print('=' * 20)
pc = randint(1, 10)
jogadas = 4
while True:
    num = int(input('Digite um número: [1-10] '))
    jogadas -= 1
    if num == pc:
        print('Parabéns, Você acertou :D')
        break
    elif jogadas == 0:
        print('Você perdeu :C')
        break
    print('Você errou :C')
    print(f'Você tem {jogadas} tentativa(s) restante(s)')