'''Faça um algoritmo que pergunte a distância que um passageiro deseja
percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para
viagens até 200Km e R$0.45 para viagens mais longas.'''
distancia = float(input('Distância que deseja percorrer: '))
if distancia < 200:
    print(f'Sua viagem custará R$ {distancia * 0.5:.2f}')
else:
    print(f'Sua viagem custará R$ {distancia * 0.45:.2f}')