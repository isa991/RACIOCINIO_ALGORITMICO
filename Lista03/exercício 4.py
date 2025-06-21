'''
Imprima os números múltiplos de 4 existentes no intervalo aberto de 1 a 100.
'''

numero = 0
soma = 4

while numero < 100:
    numero = soma + numero
    if numero % 4 == 0:
        print(numero)

