'''
Elabore um algoritmo que leia um conjunto de 10 números inteiros. Mostre então
qual o valor da soma e da média aritmética do conjunto.
'''
print('Insira um conjunto de 10 números inteiros:')
soma = 0
c = 0

while c <= 10:
    numeros = int(input('NÚMERO: '))
    soma += numeros
    c += 1
    media = soma / 10
    if c == 10:
        print('O valor da soma deste conjunto é igual a: ', soma)
        print('A média aritmética deste conjunto é igual a: ', media)
        break
