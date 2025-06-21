'''
Em um determinado estacionamento a primeira hora custa R$ 8,00, que é o valor mínimo
praticado. Após uma hora o valor é fracionado, R$ 1,50 a cada 15 minutos. Elabore um
algoritmo que leia um número inteiro correspondente a quantidade de minutos usados no
estacionamento e mostre a mensagem “Valor mínimo, R$ 8,00” ou “Valor fracionado, R$
x”, no qual x será o valor a pagar calculado pelo algoritmo.
'''

print('Para saber o valor a ser pago neste estacionamento, insira a informação abaixo, sabendo que o valor mínimo a ser pago é de R$8 reais até uma hora.')

minutos = int(input('Insira a quantidade de minutos usados no estacionamento: '))
valorFracionado = 1.5 * ((minutos - 60) // 15)
valorTotal = 8 + valorFracionado

if minutos <= 60:
    print('O valor a ser pago é de R$8 reais.')
elif minutos > 60:
    print('O valor total a ser pago é de: R$', valorTotal)
