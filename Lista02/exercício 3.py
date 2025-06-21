'''
Elabore um algoritmo que leia um número inteiro e mostre sua raiz quadrada (informe
“Valor inválido” para números negativos).
'''

numeroInteiro = int(input('Informe a seguir o número inteiro do qual deseja extrair a raiz quadrada: '))

raizQuadrada = numeroInteiro ** (1/2)
if raizQuadrada < 0:
    print('Valor inválido.')
else:
    print('A raiz quadrada do número é igual a: ', raizQuadrada)
