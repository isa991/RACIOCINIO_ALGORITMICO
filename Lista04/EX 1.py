'''
1. Construa a tabela de multiplicação de 1 a 10. (Ex: 1x1 = 1, 1x2=2, 10x10 =100)
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



