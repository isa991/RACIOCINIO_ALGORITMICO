'''
Elabore um programa que preencha uma matriz quadrada (4x4) de números inteiros, sorteados dentro
do intervalo 100 a 999, garantindo que não haverá nenhuma repetição (os 16 números devem ser
únicos). Encontre então o valor do menor elemento da linha em que se encontra o maior elemento da
matriz. Mostre a matriz e os dois valores encontrados.
'''

import random

m = []

for i in range(0,4):
    linha_m = []
    for j in range(0,4):
        linha_m.append(random.randint(100,999))
    m.append(linha_m)

maior = m[0][0] ## define o maior elemento que vai ser procurado
linha = 0       ## define a linha do maior elemento

for i in range(0,4):
    for j in range(0,4):
        if m[i][j] > maior: ## encontra o maior elemento
            maior = m[i][j] ## atribui o valor do maior elemento à sua variável
            linha = i       ## atribui o valor da linha à sua variável

menor = m[linha][0] ## define o menor elemento que vai ser procurado na linha do maior elemento
for j in range(0,4):
    if m[linha][j] < menor:
        menor = m[linha][j]

print('\nMATRIZ: ')
for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i][j],end=' | ')
    print('')

print(f'O maior elemento da matriz é: {maior}, localizado na linha: {linha}\nO elemento de menor valor nesta linha é: {menor}')