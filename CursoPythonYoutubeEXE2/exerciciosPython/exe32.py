# EXERCICIO 32
ano = int(input('Digite em que ano você está : '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Você está em um ano bissexto!')
else:
    print('Você não esta em um ano bissexto')