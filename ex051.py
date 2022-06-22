#Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela qual foi o maior e qual foi o menor preço digitados.
num = 1
maior = 0
menor = 0
while num <= 8:
    valor = int(input('Digite um valor: '))
    if num == 1:
        maior = valor
        menor = valor
    elif valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    num += 1
print(f'{maior} é o maior valor e {menor} é o menor valor')