'''Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
para todos, mas especialmente para mulheres. Faça um programa que leia nome,
sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo
que:
 - Homens ganham 5% de desconto
 - Mulheres ganham 13% de desconto'''
nome = input('Digite seu nome: ')
sexo = input('Digite seu sexo: [M/F] ').upper()
preco = float(input('Digite o preço da sua compra: '))
if sexo == 'M':
    print(f'Com o desconto de 5%, sua compra ficará por R${preco - (preco * 0.05)}')
else:
    print(f'Com o desconto de 13%, sua compra ficará por R${preco - (preco * 0.13)}')