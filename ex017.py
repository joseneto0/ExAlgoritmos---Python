#Inicio Condições Básicas
#Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
velocidade = float(input('Qual a velocidade? '))
if velocidade > 80:
    print(f'\033[1;31mMULTA\033[m. Você terá que pagar R$ {(velocidade - 80) * 5}')
else:
    print('Tudo certo :D')