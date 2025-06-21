'''
Em uma determinada loja de eletrodomésticos, os produtos podem ser adquiridos da
seguinte forma:
Elabore um algoritmo que leia a opção do cliente e o preço de tabela do produto, mostrando
então o valor calculado conforme a condição escolhida.
'''

valorProduto = float(input('Qual o valor do produto que será adquirido? '))

print('Para adquirir o produto, escolha uma das seguintes opções de pagamento:')
print(' 1 . CONDIÇÃO: À vista - CÁLCULO: 8% de desconto')
print(' 2 . CONDIÇÃO: Em 2 parcelas - CÁLCULO: 4% de desconto, dividido em duas vezes')
print(' 3 . CONDIÇÃO: Em 3 parcelas - CÁLCULO: sem desconto, dividido em três vezes')
print(' 4 . CONDIÇÃO: Em 4 parcelas - CÁLCULO: 4% de acréscimo, dividido em quatro vezes')

opcao = int(input('Escolha entre uma das opções: '))
if opcao == 1:
    valorTotal = valorProduto
    valorOpcao = (valorProduto - (valorProduto * 0.08))
    print('O valor total é igual a: ', valorTotal)
    print('Com o desconto, este valor é equivalente a: ', valorOpcao)
elif opcao == 2:
    valorTotal = (valorProduto - (valorProduto * 0.04))
    valorOpcao = ((valorProduto - (valorProduto * 0.04)) / 2)
    print('O valor total, com o desconto, é igual a: ', valorTotal)
    print('Em 2 parcelas, este valor é equivalente a: ', valorOpcao)
elif opcao == 3:
    valorTotal = valorProduto
    valorOpcao = (valorProduto / 3)
    print('O valor total é igual a: ', valorTotal)
    print('Em 3 parcelas, este valor é equivalente a: ', valorOpcao)
elif opcao == 4:
    valorTotal =(valorProduto + (valorProduto * 0.04))
    valorOpcao = ((valorProduto + (valorProduto * 0.04)) / 4)
    print('O valor total, com o acréscimo, é igual a: ', valorTotal)
    print('Em 4 parcelas, este valor é equivalente a: ', valorOpcao)
else:
    print('O número inserido é inválido. Tente novamente.')




