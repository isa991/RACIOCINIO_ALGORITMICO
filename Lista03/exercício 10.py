'''
Uma empresa de câmbio permite a compra de dólares, libras e euros. Elabore um
algoritmo que leia o código da moeda que o cliente quer comprar e qual o montante
que ele quer adquirir nessa moeda. Mostre então quanto ele deverá pagar em reais
para concretizar a operação. Além da cotação, a empresa cobra uma comissão de 5%
(quando o valor for menor que R$ 1.000), ou de 3% (quando maior ou igual a
R$1.000). Considere o câmbio do dia.
'''

print('Para escolher a opção (DÓLAR), insira (1). ')
print('Para escolher a opção (LIBRAS), insira (2). ')
print('Para escolher a opção (EUROS), insira (3). ')

cambio = int(input('CÂMBIO: '))

if cambio == 1: #dólar = 5.67
    valor = int(input('Quanto pretende adquirir dessa moeda? '))
    cotacao = valor * 5.67
    if valor < 1000:
        valorTotal = (cotacao * 0.05) + cotacao
        print('O valor total para adquirir esta quantidade de dólares em reais é de: ', valorTotal)
    else:
        valorTotal = (cotacao * 0.03) + cotacao
        print('O valor total para adquirir esta quantidade de dólares em reais é de: ', valorTotal)
if cambio == 2: #libras = 7.35
    valor = int(input('Quanto pretende adquirir dessa moeda? '))
    cotacao = valor * 7.35
    if valor < 1000:
        valorTotal = (cotacao * 0.05) + cotacao
        print('O valor total para adquirir esta quantidade de libras em reais é de: ', valorTotal)
    else:
        valorTotal = (cotacao * 0.03) + cotacao
        print('O valor total para adquirir esta quantidade de libras em reais é de: ', valorTotal)
if cambio == 3: #euros = 6.13
    valor = int(input('Quanto pretende adquirir dessa moeda? '))
    cotacao = valor * 6.13
    if valor < 1000:
        valorTotal = (cotacao * 0.05) + cotacao
        print('O valor total para adquirir esta quantidade de euros em reais é de: ', valorTotal)
    else:
        valorTotal = (cotacao * 0.03) + cotacao
        print('O valor total para adquirir esta quantidade de euros em reais é de: ', valorTotal)
