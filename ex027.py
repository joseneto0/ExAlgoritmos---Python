'''Crie um programa que leia duas notas de um aluno e calcule a sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média até 4.9: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''
nota1 = float(input('Digite sua 1° nota: '))
nota2 = float(input('Digite sua 2° nota: '))
media = (nota1 + nota2) / 2
print(f'Sua média é {media:.1f}')
if media <= 4.9:
    print('\033[1;31mREPROVADO\033[m')
elif media <= 6.9:
    print('\033[1;91mRECUPERAÇÃO\033[m')
else:
    print('\033[1;32mAPROVADO :D\033[m')