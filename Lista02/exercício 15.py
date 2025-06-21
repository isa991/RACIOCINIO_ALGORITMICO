'''
15.Escreva um algoritmo que leia três números inteiros e mostre-os em ordem decrescente.
'''

numero_Um = (int(input('Insira o primeiro número inteiro: ')))
numero_Dois = (int(input('Insira o segundo número inteiro: ')))
numero_Tres = (int(input('Insira o terceiro número inteiro: ')))

if numero_Um >= numero_Dois and numero_Um >= numero_Tres:
    if numero_Dois >= numero_Tres:
        print('Os números inseridos em ordem decrescente são: ', numero_Um, numero_Dois, numero_Tres)
    else:
        print('Os números inseridos em ordem decrescente são: ', numero_Um, numero_Tres, numero_Dois)
elif numero_Dois >= numero_Um and numero_Dois >= numero_Tres:
    if numero_Um >= numero_Tres:
        print('Os números inseridos em ordem decrescente são: ', numero_Dois, numero_Um, numero_Tres)
    else:
        print('Os números inseridos em ordem decrescente são: ', numero_Dois, numero_Tres, numero_Um)
else:
    if numero_Um >= numero_Dois:
        print('Os números inseridos em ordem decrescente são: ', numero_Tres, numero_Um, numero_Dois)
    else:
        print('Os números inseridos em ordem decrescente são: ', numero_Tres, numero_Dois, numero_Um)


