#A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.
km = float(input('Quantos Km rodados? '))
dias = int(input('Quantos dias o carro foi alugado? '))
print(f'O toal a pagar é R$ {km * 0.20 + dias * 90}')