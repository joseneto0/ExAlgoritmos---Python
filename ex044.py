'''Crie um algoritmo que leia o valor inicial da contagem, o valor final e o
incremento, mostrando em seguida todos os valores no intervalo:
Ex: Digite o primeiro Valor: 3
Digite o último Valor: 10
Digite o incremento: 2
Contagem: 3 5 7 9 Acabou!'''
primeiro = int(input('Digite o primeiro valor: '))
ultimo = int(input('Digite o ultimo valor: '))
incremento = int(input('Digite o incremento: '))
while primeiro <= ultimo:
    print(primeiro, end=' ')
    primeiro += incremento
print('Acabou!')