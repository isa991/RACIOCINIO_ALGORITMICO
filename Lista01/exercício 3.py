#Faça um algoritmo que recebe o valor de um produto e calcule
#os seguintes valores:
#(1) a vista com 5% de desconto;
#(2) o valor da parcela em 2x;
#(3) o valor da parcela em 3x com acréscimo de 5%.

valorProduto = int(input('Insira o valor do produto que será calculado: R$'))

valorDescontovista  = (valorProduto * 0.05)
valorVista = (valorProduto - valorDescontovista)

print('Se pago a vista, terá um desconto de 5%, sendo o valor total igual à: R$', valorVista)

valorParcela = (valorProduto / 2)

print('Se pago de forma parcelada em 2x não haverá juros, resultando em duas parcelas no valor de: R$', valorParcela)

produtoDesconto = valorProduto + valorDescontovista
valorParcela3 = (produtoDesconto / 3)

print('Se pago de forma parcelada em 3x haverá juros de 5%, resultando em três parcelas no valor de: R$', valorParcela3)