'''Faça um programa que leia a largura e o comprimento de um terreno
retangular, calculando e mostrando a sua área em m². O programa também
devemostrar a classificação desse terreno, de acordo com a lista abaixo:
- Abaixo de 100m² = TERRENO POPULAR
- Entre 100m² e 500m² = TERRENO MASTER
- Acima de 500m² = TERRENO VIP'''
largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
area = largura * comprimento
print('=' * 12)
print(f'Área: {area}m²')
if area < 100:
    print('Seu Terreno é POPULAR')
elif area <= 500:
    print('Seu Terreno é MASTER')
else:
    print('Seu Terreno é VIP')