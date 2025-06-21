'''
2. Construa a tabela de multiplicação de 1 a 10 utilizando apenas um laço de repetição.
'''

x = 0
n = 1
c = 1


while x < 10 and c <= 10:
    x += 1
    n = (c * x)
    print(c, 'x', x, '=', n)
    if x == 10:
        print(' ')
        x = 0
        c += 1