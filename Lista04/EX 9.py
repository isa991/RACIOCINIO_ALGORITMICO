'''
Desenvolva um programa que leia 10 números inteiros e armazene-os em um vetor chamado vLido.
Depois, crie dois outros vetores: vPares, contendo somente os números pares de vLido, e vImpares
contendo somente os números ímpares de vLido. Os vetores vPares e vLido não deverão conter
zeros. Mostre então os três vetores.
'''

vLido = []
vPares = []
vImpares = []

for i in range(0,10):
    n = int(input(f'Insira o {i+1}° valor inteiro: '))
    if n != 0:
        vLido.append(n)
        if n % 2 == 0:
            vPares.append(n)
        else:
            vImpares.append(n)

print('Os valores do vetor lido são: ', vLido)
print('Os valores do vetor de números pares são: ', vPares)
print('Os valores do vetor de números ímpares são: ', vImpares)