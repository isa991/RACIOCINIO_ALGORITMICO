'''
Implemente um programa que permita multiplicar uma matriz de ordem (3×3) de números inteiros
fornecida pelo usuário por um número também fornecido pelo usuário.

Lembrete: para multiplicar uma matriz Am×n por um escalar k, basta multiplicar cada entrada aij
de A por k. Assim, a matriz resultante B será também da ordem (m×n) e bij = k * aij.
'''

ma = []  ##A3x3 * n = B3x3
mb = []  ##B3x3

for i in range(0,3):
    linha_ma = []
    for j in range(0,3):
        num = int(input(f'Insira o {j+1}° número da matriz 3x3: '))
        linha_ma.append(num)
    ma.append(linha_ma)

k = int(input('\nInsira o número inteiro pelo qual deseja multiplicar a matriz: '))

for i in range(0,3):
    linha_mb = []
    for j in range(0,3):
        multi = ma[i][j] * k
        linha_mb.append(multi)
    mb.append(linha_mb)

print('\nMATRIZ A(3x3): ')
for i in range(len(ma)):
    for j in range(len(ma[0])):
        print(ma[i][j],end=' | ')
    print('')

print('\nMATRIZ A * K = B(3x3): ')
for i in range(len(mb)):
    for j in range(len(mb[0])):
        print(mb[i][j],end=' | ')
    print('')