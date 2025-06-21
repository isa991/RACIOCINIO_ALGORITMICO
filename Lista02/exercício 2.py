'''
A partir do ano de nascimento informado pelo usuário, elabore um algoritmo que informe
a idade que completará (ou já completou) em 2023. Verifique se ele já pode fazer a carteira
de motorista ou não, informando sua situação.
'''

anoNascimento = int(input('Insira o seu ano de nascimento: '))
anoDesejado = 2023
anoAtual = 2025

idade2025 = (anoAtual - anoNascimento)
idade2023 = (anoDesejado - anoNascimento)

print('Você já completou a idade de: ', idade2023 , 'anos em 2023.')
print('Você tem atualmente: ', idade2025 , 'anos.')

if idade2025 >= 18:
    print('Parabéns! Você já pode fazer sua carteira de motorista.')
else:
    print('Você ainda não pode fazer sua carteira de motorista por ser menor de idade.')
