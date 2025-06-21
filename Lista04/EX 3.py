'''
3. Leia três números do teclado e verificar
se o primeiro é maior que a soma dos outros dois.
'''

n1 = int(input('Insira o primeiro número inteiro: '))
n2 = int(input('Insira o segundo número inteiro: '))
n3 = int(input('Insira o terceiro número inteiro: '))

soma = n2 + n3

if n1 > soma:
    print('O primeiro número é maior que a soma dos outros dois números.')
else:
    print('O primeiro número não é maior do que a soma dos outros dois números.')