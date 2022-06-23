'''Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários.
No final, mostre o total de salários pagos aos homens e o total pago às
mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não
sempre que ler os dados de um funcionário.'''
soma_homens = 0
soma_mulheres = 0
while True:
    salario = float(input('Digite o salário: '))
    sexo = input('Digite seu sexo: [F/M] ').upper()
    while sexo not in 'FM':
        sexo = input('Tente Novamente. Digite seu sexo: [F/M] ')
    if sexo == 'M':
        soma_homens += 1
    elif sexo == 'F':
        soma_mulheres += 1
    continuar = input('Quer continuar? [S/N] ').upper()
    if continuar == 'N':
        break
print(f'Total de pessoas cadastradas: {soma_homens + soma_mulheres}')
print(f'Total de homens: {soma_homens}')
print(f'Total de mulheres: {soma_mulheres}')