# EXERCICIO 28
from random import randint
a = randint(1, 6)
print('O computador pesou em um numero de 1 a 6. Tente adivinhar')
n = int(input('Digite o numero que você acha que o computador pensou : '))
# OPÇÃO 1
# print('Você acertou o resultado era {}!'.format(a) if n == a else 'O computador venceu o resultado era {}'.format(a))
# OPÇÃO 2
# if n == a:
#     print('Você acertou o resultado era {}!'.format(a))
# else:
#     print('Você perdeu o resultado era {}'.format(a))    
# OPÇÃO 3

erros = 0
while n != a:
    erros = erros + 1
    print('Você errou. Tente novamente')
    n = int(input('Digite o numero que você acha que o computador pensou : '))
if n == a:
    print('Parabéns, você acertou com {} erros!. O resultado era {}'.format(erros, a))