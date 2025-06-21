'''
Imprima uma tabela de conversão de polegadas para centímetros, cuja escala vai de
1 a 20 polegadas. A conversão entre estas duas unidades é dada por: polegada =
centímetro × 2,54
'''

polegada = 0

while polegada < 20:
    polegada += 1
    cm = polegada * 2.54
    print('O número de polegadas (',polegada,'), em centímetros, é igual a: ', cm)


