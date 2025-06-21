'''
6. Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é
triangular.
'''

n = int(input('Insira um número inteiro não-negativo: '))
if n < 0:
    n= int(input('Número inválido. Insira um número positivo.'))

triangular = 0
x = 1

while triangular < n:
    triangular = (x * (x + 1) * (x + 2))
    x += 1

if triangular == n:
    print('O número inteiro inserido é triangular.')
else:
    print('O número inteiro inserido não é triangular.')