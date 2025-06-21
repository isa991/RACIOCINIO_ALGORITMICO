'''
Escreva um programa que preencha uma matriz quadrada de números inteiros de dimensão (5×5)
com valores inteiros (dentro do intervalo 10 a 99). Para cada uma das figuras abaixo (elabore quatro
versões do programa): mostre a matriz original, mostre a matriz apenas com os valores que estão na
parte hachurada e mostre a soma destes valores:

V4
'''

import random

m = []

for i in range(0,5):
    linha_m = []
    for j in range(0,5):
        linha_m.append(random.randint(10,99))
    m.append(linha_m)

print('\nMATRIZ ORIGINAL: ')
for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i][j],end=' | ')
    print('')

v = []

print('\nMATRIZ HACHURADA D: ')
for i in range(len(m)):
    for j in range(len(m[0])):
        if i - j == 1 or j - i == 1 or i - j == 3 or j - i == 3:
            print(m[i][j], end=' | ')
            v.append(m[i][j])
        else:
            print('--', end=' | ')
    print(' ')

##SOMA DOS VALORES
print(f'\nA soma dos valores da lista hachurada é igual a: {sum(v)}')