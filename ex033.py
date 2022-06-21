'''Escreva um programa para aprovar ou não o empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
ela não pode exceder 30% do salário ou então o empréstimo será negado.'''
casa = float(input('Valor da casa: '))
salario = float(input('Sálario: '))
anos = int(input('Anos para pagar a casa: '))
prestacao = casa / (anos * 12)
print(f'Você terá que pagar R$ {prestacao:.2f}, durante {anos * 12} meses')
if salario * (30/100) > prestacao:
    print(f'Você tem condição de pagar o empréstimo')
    print('Empréstimo APROVADO :D')
else:
    print('Você não tem condição de pagar o empréstimo')
    print('Empréstimo REPROVADO :C')