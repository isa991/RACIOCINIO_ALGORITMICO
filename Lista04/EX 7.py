'''
7. A Amplitude amostral é uma médida de dispersão, ela é calculada como a diferença entre o valor
máximo e o valor mínimo de uma amostra. Elabore um programa que leia um vetor de 10 posições
inteiras e então mostre o valor máximo, o valor mínimo e a amplitude amostral do conjunto
fornecido.
'''


listNum = []

for i in range(0, 10):
    vetor = int(input(f'Insira a {i+1}° posição inteira do vetor: '))
    listNum.append(vetor)
ampAmostral = max(listNum) - min(listNum)

print('O valor máximo do conjunto do o vetor foi igual a: ', max(listNum))
print('O valor mínimo do conjunto do o vetor foi igual a: ', min(listNum))
print('A amplitude amostral do conjunto é igual a: ', ampAmostral)

## ampAmostral = max(listNum) - min(listNum)