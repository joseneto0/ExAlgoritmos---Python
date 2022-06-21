'''37) Uma empresa precisa reajustar o salário dos seus funcionários, dando um
aumento de acordo com alguns fatores. Faça um programa que leia o salário atual,
o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa.
No final, mostre o seu novo salário, baseado na tabela a seguir:
- Mulheres
- menos de 15 anos de empresa: +5%
- de 15 até 20 anos de empresa: +12%
- mais de 20 anos de empresa: +23%
- Homens
- menos de 20 anos de empresa: +3%
- de 20 até 30 anos de empresa: +13%
- mais de 30 anos de empresa: +25%'''
salario = float(input('Digite seu salário atual: '))
sexo = input('Digite seu sexo: [M/F] ').upper()
anos = int(input('Anos de trabalho na empresa: '))
if sexo == 'F':
    if anos < 15:
        salario_novo = salario + (salario * 0.05)
        print('Você recebeu um aumento de 5%')
    elif anos <= 20:
        salario_novo = salario + (salario * 0.12)
        print('Você recebeu um aumento de 12%')
    else:
        salario_novo = salario + (salario * 0.23)
        print('Você recebeu um aumento de 23%')
elif sexo == 'M':
    if anos < 20:
        salario_novo = salario + (salario * 0.03)
        print('Você recebeu um aumento de 3%')
    elif anos <= 30:
        salario_novo = salario + (salario * 0.13)
        print('Você recebeu um aumento de 12%')
    else:
        salario_novo = salario + (salario * 0.25)
        print('Você recebeu um aumento de 25%')
print(f'Você vai receber R$ {salario_novo:.2f} de salário')