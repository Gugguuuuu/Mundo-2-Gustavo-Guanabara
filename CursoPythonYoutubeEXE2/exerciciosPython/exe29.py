# EXERCICIO 29
km = float(input('Digite quantos quilometros estava o carro : '))
l= int(input('Digite qual era o limite de velocidade : '))
moeda = str(input('Qual é a sua moeda? '))
moeda = moeda.lower()
moeda = moeda.strip()
m = (km - l) * 7
if moeda == 'real':
    moeda = 'reais'
elif moeda == 'libra':
    moeda = 'libras'
elif moeda == 'dolar':
    moeda = 'dolares'
elif moeda == 'euro':
    moeda = 'euros'
elif moeda == 'peso argentino':
    moeda = 'pesos argentinos'
if km > l:
    print('Você estava acima da velocidade sua multa sera de {:.1f} {}'.format(m, moeda))
if km == l:
    print('Você esta na faixa de velocidade')
elif km < l:
    print('Você esta abaixo da faixa e velocidade, continue assim')