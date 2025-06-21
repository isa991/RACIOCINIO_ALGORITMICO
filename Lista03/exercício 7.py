'''
Considerando que 1 milha vale exatamente 1.609,344 metros, imprima uma tabela
de conversão de metros (m) para milhas (mi.), de 20 km até 160 km, de 10 em 10
quilômetros.
'''

metros = 10000

#20km -> 20000m
while metros < 20000 or metros < 160000:
    metros += 10000
    milha = metros / 1.6
    km = metros / 1000

    print('O valor em quilômetros (',km,'), em milhas é igual a: ', milha)




