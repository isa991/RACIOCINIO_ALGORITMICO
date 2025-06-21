'''
Em uma determinada papelaria a fotocópia custa R$ 0,25, caso sejam tiradas menos de 100
cópias. A partir de 100 cópias, o valor de cada fotocópia tirada cai para R$ 0,20. Elabore
um algoritmo que leia o número de cópias e mostre o valor a pagar pelo serviço.
'''

print('Para calcular o valor a ser pago pela fotocópia, insira a seguinte informação abaixo.')

copias = int(input('Qual o número de cópias a serem tiradas? '))

if copias < 100:
    valorCopia = (0.25 * copias)
else:
    valorCopia = (0.20 * copias)

print('O valor a ser pago por essa quantidade de fotocópias é de: R$', valorCopia)