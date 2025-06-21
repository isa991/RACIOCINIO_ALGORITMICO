'''
5. Ler 4 números inteiros e calcular a soma dos que forem par.
'''

n1 = int(input('Insira o primeiro número inteiro: '))
n2 = int(input('Insira o segundo número inteiro: '))
n3 = int(input('Insira o terceiro número inteiro: '))
n4 = int(input('Insira o quarto número inteiro: '))

soma = 0

if n1 % 2 == 0:
    soma = soma + n1
if n2 % 2 == 0:
    soma = soma + n2
if n3 % 2 == 0:
    soma = soma + n3
if n4 % 2 == 0:
    soma = soma + n4

print('A soma de todos os valores pares é igual a: ', soma)

