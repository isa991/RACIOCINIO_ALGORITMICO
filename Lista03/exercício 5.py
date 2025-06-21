'''
Imprima os números ímpares de 1 até n, sendo n fornecido pelo usuário.
'''

n = int(input('Insira um número: '))
numero = -1
soma = 2
numeroPar = 1

while n > numero and n > numeroPar:
    if n % 2 == 0:
        numeroPar = numeroPar + soma
        print(numeroPar - 2)
    else:
        numero = numero + soma
        print(numero)