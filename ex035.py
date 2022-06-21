'''Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O
aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para
carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e
quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a
tabela a seguir:
- Carros populares (aluguel de R$90 por dia)
- Até 100Km percorridos: R$0,20 por Km
- Acima de 100Km percorridos: R$0,10 por Km
- Carros de luxo (aluguel de R$150 por dia)
- Até 200Km percorridos: R$0,30 por Km
- Acima de 200Km percorridos: R$0,25 por Km'''
carro = input('Qual o tipo do carro? [P/L] ').upper()
dias = int(input('Quantos dias você alugou o carro? '))
km = float(input("Quantos km's foram percorridos: "))
if carro == 'P':
    if km < 100:
        total = dias * 90 + km * 0.20
        print(f'Sua conta deu R$ {total:.2f}')
    else:
        total = dias * 90 + km * 0.10
        print(f'Sua conta deu R$ {total:.2f}')
else:
    if km < 200:
        total = dias * 150 + km * 0.30
        print(f'Sua conta deu R$ {total:.2f}')
    else:
        total = dias * 150 + km * 0.25
        print(f'Sua conta deu R$ {total:.2f}')