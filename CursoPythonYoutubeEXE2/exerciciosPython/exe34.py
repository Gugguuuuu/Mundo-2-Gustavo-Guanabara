# EXERCICIO 34
n = int(input('Digite um numero : '))
pi = n % 2

if pi == 0:
    print('O numero {}, é par'.format(n))
else:
    print('O numero {}, é impar'.format(n))