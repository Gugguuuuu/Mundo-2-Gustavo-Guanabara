# EXERCICIO 33
ask = str(input('Você vai fazer compras? (\033[1;32ms\033[m/\033[1;31mn\033[m)')).strip().lower()
i = media = soma = media = 0
while ask == 's':
    i += 1
    compra = float(input('Digite o valor da {}° compra :'.format(i)))
    soma += compra
    ask = str(input('Você fez mais compras? (\033[1;32ms\033[m/\033[1;31mn\033[m)')).strip().lower()
media = soma / i
print('A media das suas compras foi {:.2f}'.format(media))
