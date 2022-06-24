'''Crie um programa que preencha automaticamente (usando lógica, não apenasb atribuindo diretamente um vetor numérico com 15 posições com os primeiros elementos da sequência de Fibonacci:'''
lista = []
n1 = 1
n2 = 1
lista.append(n1)
lista.append(n2)
for i in range(14):
    fibo = n1 + n2
    n1 = n2
    n2 = fibo
    lista.append(fibo)
print(lista)