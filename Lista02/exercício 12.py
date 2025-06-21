'''
A partir das informações contidas na tabela abaixo, elabore um algoritmo que leia a
massa em kg de um boxeador e mostre a qual categoria ele pertence. Caso ele não se
encaixe, informe “Categoria inferior a Super-médio”. Lembrando que 1 quilograma =
2,20462262 libras.
'''

massa = float(input('Qual é a sua massa? (em KG) '))
massaLb = (massa * 2.20462262) #kg -> libras
if massaLb < 161:
    categoria = 'Inferior a Super-médio'
elif 161 <= massaLb <= 168:
    categoria = 'Super-médio'
elif 169 <= massaLb <= 175:
    categoria = 'Meio-pesado'
elif 176 <= massaLb <= 200:
    categoria = 'Cruzador'
else:
    categoria = 'Peso-pesado'

print('Sua massa, em libras, é igual a: ', massaLb )
print('De acordo com a sua massa, em libras, sua categoria é: ', categoria)


