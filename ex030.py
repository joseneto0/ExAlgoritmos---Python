'''[DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais
- ESCALENO: todos os lados diferentes'''
seg1 = float(input('Digite o primeiro segmento: '))
seg2 = float(input('Digite o segundo segmento: '))
seg3 = float(input('Digite o terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('É possível formar um triângulo :)')
    if seg1 == seg2 == seg3:
        print('Seu triângulo é EQUILÁTERO')
    elif (seg1 == seg2 and seg1 != seg3 and seg2 != seg3) or (seg1 == seg3 and seg1 != seg2 and seg3 != seg2) or (seg2 == seg3 and seg2 != seg1 and seg3 != seg1):
        print('Seu triângulo é ISÓSCELES')
    else:
        print('Seu triângulo é ESCALENO')
else:
    print('Não é possível formar um triângulo :(')