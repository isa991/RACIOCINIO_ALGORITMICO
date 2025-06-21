'''
O IMC (Índice de Massa Corporal) é calculado através da seguinte fórmula:
IMC = massa / altura2
Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do usuário
e mostre o valor do IMC e se ele está na faixa considerada “normal” segundo o critério
apresentado na tabela da OMS (Organização Mundial de Saúde): 18,5 ≤ IMC< 25. Caso
não esteja, calcule sua massa máxima considerada normal (usando IMC igual a 24,9).
'''

massa = float(input('Qual a valor de sua massa? (em KG) '))
altura = float(input('Qual a sua altura? (em metros) '))

imc = (massa / (altura * altura))

print('Seu imc é igual a: ', imc )
if 18.5 <= imc < 25:
    print('Seu imc está na faixa considerada "normal".')
elif imc > 25:
    massaMaxima = 24.9 * (altura * altura)
    print('A sua massa máxima considerada normal é igual a: ', massaMaxima , 'kg.')
