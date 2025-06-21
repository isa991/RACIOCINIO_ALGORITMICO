'''
14.Escreva um algoritmo que leia três números inteiros e mostre o valor do maior deles.
'''

numeroUm = int(input('Insira o primeiro número inteiro: '))
numeroDois = int(input('Insira o segundo número inteiro: '))
numeroTres = int(input('Insira o terceiro número inteiro: '))

if numeroUm >= numeroDois and numeroUm >= numeroTres:
    print('O maior número é: ', numeroUm)
elif numeroDois >= numeroUm and numeroDois >= numeroTres:
    print('O maior número é: ', numeroDois)
else:
    print('O maior número é: ', numeroTres)


