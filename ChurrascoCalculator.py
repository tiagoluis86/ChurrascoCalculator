print('CHURRASCO CALCULATOR')

pessoas = int(input('Quantas pessoas vão no churrasco?'))
carne = pessoas*300
cerveja = pessoas*6

print('Então serão necessários {}g de carne e {} latinhas de cerveja'.format(carne, cerveja))

precoCarne = float(input('Quanto está custando o kg da carne?'))
precoCerveja = float(input('Quanto está custando a cerveja?'))

precoChurrasco = precoCarne*carne/1000 + cerveja*precoCerveja
precoPessoa = precoChurrasco / pessoas

if precoChurrasco >= 1000:
    print('Seu churrasco vai custar ao todo {}, sendo {} por pessoa' .format(precoChurrasco, precoPessoa))
    print('Caro pra carai, boa sorte!!!!')
else:
    print('Seu churrasco vai custar ao todo {}, sendo {} por pessoa'.format(precoChurrasco, precoPessoa))
    print('Vai na fé!!!!')