'''
Escreva um programa que popule uma matriz (15×7) de números inteiros sorteados dentro do
intervalo 10 a 99. Modifique então a matriz de forma que, caminhando da esquerda para a direita, de
cima para baixo, tenhamos primeiro todos os números pares, depois, os números impares. Mostre a
matriz antes e depois da modificação.
'''

import random

m = []
vPar = []
vImp = []
mOrd = []

for i in range(0,15):
    linha_m = []
    for j in range(0,7):
        linha_m.append(random.randint(10,99))
    m.append(linha_m)

for lin in m:
    for num in lin:
        if num % 2 == 0:
            vPar.append(num)
        else:
            vImp.append(num)

all_num = vPar + vImp

k = 0
for i in range(15):
    linha_mOrd = []
    for j in range(7):
        linha_mOrd.append(all_num[k])
        k += 1
    mOrd.append(linha_mOrd)

print('\nMATRIZ: ')
for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i][j],end=' | ')
    print('')

print('\nMATRIZ ORDENADA (PARES & IMPARES): ')
for i in range(len(mOrd)):
    for j in range(len(mOrd[0])):
        print(mOrd[i][j],end=' | ')
    print('')
