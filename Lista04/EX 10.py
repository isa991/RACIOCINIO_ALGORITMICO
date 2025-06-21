'''
Escreva um programa que leia um vetor de números inteiros de 10 posições, aceitando apenas
valores positivos. Modifique então o vetor de forma que, tenhamos primeiro todos os números pares,
depois, os números impares. Mostre o vetor antes de depois da modificação.
'''

vLido = []
vPares = []
vImpares = []
vOrdem = []

for i in range(0,10):
    num = int(input(f'Insira o {i+1}° número inteiro: '))
    if num > 0:
        vLido.append(num)
        if num % 2 == 0:
            vPares.append(num)
        else:
            vImpares.append(num)
vOrdem.append(vPares)
vOrdem.append(vImpares)

print('Os valores originais do vetor são igual a: ', vLido)
print('O vetor ordenado em pares e ímpares é igual a: ', vOrdem)