'''
Tendo como dados de entrada a altura (h) e o sexo de uma pessoa (use 1 - masculino e 2 -
feminino) elabore um algoritmo que calcule o peso ideal (p) do usuário utilizando as
seguintes fórmulas:
a. para homens: p = (72.7 * h) - 58
b. para mulheres: p = (62.1 * h) - 44.7
'''

print('Para calcular o seu peso ideal, insira as seguintes informações abaixo.')

altura = float(input('Qual sua altura? (em metros) '))

pesoIdealhomem = (72.7 * altura) - 58
pesoIdealmulher = (62.1 * altura) - 44.7

sexualidade = int(input('Se for do sexo masculino, insira 1. Se for do sexo feminino, insira 2. '))
if sexualidade == 1:
    print('Seu peso ideal é igual a: ', pesoIdealhomem, 'kg.')
elif sexualidade == 2:
    print('Seu peso ideal é igual a: ', pesoIdealmulher , 'kg.')
else:
    print('O número inserido acima é inválido. Insira 1 ou 2.')