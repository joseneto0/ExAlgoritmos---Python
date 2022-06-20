#Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.
distancia = float(input('Digite a distância em metros: '))
print(f'A distância de {distancia} corresponde a:')
print(f'{distancia/1000} Km')
print(f'{distancia/100} Hm')
print(f'{distancia/10} Dam')
print(f'{distancia*10} dm')
print(f'{distancia*100} cm')
print(f'{distancia*1000} mm')