#Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.
produto = float(input('Digite o preço do produto: R$ '))
print(f'O produto com desconto de 5% fica por R$ {produto - (produto * 0.05)}')