#Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.
salario = float(input('Digite o salário do funcionário: R$ '))
print(f'O salário com aumento de 15% ficará R$ {salario + (salario * (15/100))}')