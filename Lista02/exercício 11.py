'''
Elabore um algoritmo que, dada a idade de um nadador, mostre sua classificação
segundo uma das seguintes categorias:
• 5 até 7 anos: Infantil A;
• 8 até 10 anos: Infantil B;
• 11 até 13 anos: Juvenil A;
• 14 até 17 anos: Juvenil B;
• Maiores de 18 anos: Adulto.
'''

print('Para descobrir sua classificação como nadador, insira a seguinte informação.')

idade = int(input('Qual a sua idade? '))
if idade < 5:
    classificacao = 'Não há classificação para uma criança abaixo de 5 anos.'
elif 5 <= idade <= 7:
    classificacao = 'Infantil A'
elif 8 <= idade <= 10:
    classificacao = 'Infantil B'
elif 11 <= idade <= 13:
    classificacao = 'Juvenil A'
elif 14 <= idade <= 17:
    classificacao = 'Juvenil B'
else:
    classificacao = 'Adulto'

print('A sua classificação, de acordo com sua faixa etária, é igual a: ', classificacao)