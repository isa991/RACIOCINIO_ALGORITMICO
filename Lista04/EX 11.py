'''
Construa um programa que sugira uma aposta de Mega-Sena ou seja, um algoritmo que gera e mostra
um conjunto de 6 números aleatórios entre [1, 60] sem repetição. Em seguida, obtenha a aposta do
usuário (sem repetição) e indique quantos acertos ele teve.
'''

import random

aposta = set()
mega = sorted(random.sample(range(1,60),6))

x = 0

while x < 6:
    print(mega)
    num = int(input(f'Insira o {x+1}° número da aposta: '))
    if num < 60:
        aposta.add(num)
        x += 1
    print(aposta)

acertos = set(mega) & set(aposta)

print('A sua aposta compôs o seguinte conjunto de números: ', aposta)
print('Dos números apostados, você acertou um total de: ',  len(acertos))
if acertos == 6:
    print('Parabéns! Você obteve 100% de acertos!')


##mega_sena = sorted(random.sample(range(1, 61),6))


