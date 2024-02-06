# EXERCICIO 31
v = float(input('Digite a distancia em quilometros da sua viagem : '))

if v <= 200.0:
    print('O valor da passagem sera {:.2f} reais.'.format(v * 0.5))
elif v > 200.0:
    print('O valor da passagem sera {:.2f} reais.'.format(v * 0.45))