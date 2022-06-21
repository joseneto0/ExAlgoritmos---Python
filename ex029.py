'''Desenvolva um programa que leia o nome de um funcionário, seu salário,
quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
acordo com a tabela a seguir:
- Até 3 anos de empresa: aumento de 3%
- entre 3 e 10 anos: aumento de 12.5%
- 10 anos ou mais: aumento de 20%'''
nome = input('Digite seu nome: ')
anos = int(input('Quantos anos você trabalha na empresa? '))
salario = float(input('Quanto você recebe? '))
print('=' * 20)
if anos < 3:
    print(f'Você ganhou um aumento de 3% por trabalhar a {anos} anos na nossa empresa :)')
    print(f'Seu novo salário vai ser R$ {salario + (salario * 0.03)}')
elif anos <= 10:
    print(f'{nome}, Obrigado por confiar na nossa empresa :D')
    print(f'Você ganhou um aumento de 12.5% por trabalhar a {anos} anos na nossa empresa :)')
    print(f'Seu novo salário vai ser R$ {salario + (salario * 0.125)}')
else:
    print(f'{nome}, Obrigado por confiar na nossa empresa :D')
    print(f'Você ganhou um aumento de 20% por trabalhar a {anos} anos na nossa empresa :)')
    print(f'Seu novo salário vai ser R% {salario + (salario * 0.20)}')
