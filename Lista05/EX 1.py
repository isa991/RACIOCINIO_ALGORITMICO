'''
Desenvolva um programa que leia uma matriz quadrada de números inteiros de dimensão (4×4), e
então coloque em um outro vetor de 4 posições o maior valor encontrado na coluna da matriz cujo
índice é o mesmo do vetor, ou seja, o maior valor da coluna zero da matriz na posição zero do vetor e
assim por diante. Mostre então a matriz, o vetor e a média aritmética do vetor.
'''

m = []

for i in range(0,4):
    linha_m = []
    for j in range(0,4):
        num = int(input(f'Insira o {j+1}° número da matriz 4x4: '))
        linha_m.append(num)
    m.append(linha_m)

v = []

for col in range(0,4):
    maior = m[0][col]
    for lin in range(1,4):
        if m[lin][col] > maior:
            maior = m[lin][col]
    v.append(maior)

print('\nMATRIZ: ')
for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i][j],end=' | ')
    print('')

print(f'\nVetor c/ o maior elemento de cada coluna: {v}\nA média é: {media}')

media = sum(v) / len(v)
print('\nA média é: ', media)