#O programa acima vai ter um problema quando digitarmos o primeiro valor maior que o último. Resolva esse problema com um código que funcione em qualquer situação.
primeiro = int(input('Digite o primeiro valor: '))
ultimo = int(input('Digite o ultimo valor: '))
incremento = int(input('Digite o incremento: '))
if primeiro > ultimo:
    while primeiro >= ultimo:
        print(primeiro, end=' ')
        primeiro -= incremento
else:
    while primeiro <= ultimo:
        print(primeiro, end=' ')
        primeiro += incremento
print('Acabou!')