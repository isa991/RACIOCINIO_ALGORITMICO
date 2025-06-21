'''
A partir da idade informada de uma pessoa, elabore um algoritmo que informe a sua
classe eleitoral, sabendo que menores de 16 não votam (não votante), que o voto é
obrigatório para adultos entre 18 e 65 anos (eleitor obrigatório) e que o voto é opcional
para eleitores entre 16 e 18, ou maiores de 65 anos (eleitor facultativo).
'''

print('Para descobrir qual é a sua classe eleitoral, insira a seguinte informação.')

idade = int(input('Qual é a sua idade? '))

if idade < 16:
    classeEleitoral = 'Não votante'
elif 16 <= idade < 18:
    classeEleitoral = 'Voto opcional'
elif 18 <= idade < 65:
    classeEleitoral = 'Eleitor obrigatório'
else:
    classeEleitoral = 'Eleitor facultativo'

print('A sua classe eleitoral é: ', classeEleitoral)


