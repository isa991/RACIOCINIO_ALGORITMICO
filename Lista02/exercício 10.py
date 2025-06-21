'''
O IMC, índice de massa corporal, é calculado através da seguinte fórmula: IMC = massa /
altura2
Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do
usuário e mostre o valor do IMC e qual sua condição segundo o critério apresentado na
tabela da OMS (Organização Mundial de Saúde)
'''

print('Para descobrir qual é a sua condição segundo o critério apresentado na tabela da OMS, insira as seguintes informações.')

massa = float(input('Qual é a sua massa? (em KG) '))
altura = float(input('Qual é a sua altura? (em metros) '))

imc = massa / (altura * altura)
if imc < 18.5:
    condicao = 'Abaixo do peso'
elif 18.5 <= imc < 25:
    condicao = 'Peso normal'
elif 25 <= imc < 30:
    condicao = 'Acima do peso'
else:
    condicao = 'Obeso'

print('O valor do seu IMC é igual a: ', imc)
print('De acordo com a OMS, o seu IMC se encaixa na condição de: ', condicao)

