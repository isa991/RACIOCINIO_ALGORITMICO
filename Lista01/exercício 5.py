#Faça um algoritmo que calcule a quantidade de latas de tintas
#necessárias para pintar
#um tanque cilindro, em que são fornecidas sua altura e raio, sabendo que:

alturaCilindro = int(input('Qual a altura do cilindro? '))
raioCilindro = int(input('Qual o raio do cilindro? '))
areaCilindro = (2 * 3.14 * raioCilindro * (raioCilindro + alturaCilindro))
#área sai em m²
#3.14 = π

valorLata = 50 #reais
volumeLata = 5 #litros
pintaLata = 3 #m²

capacidadeLata = (volumeLata * pintaLata) #quantos m² pinta
quantidadeLata = (areaCilindro // capacidadeLata) #quantas precisa
custoLata = (valorLata * quantidadeLata) #custo final

print('Para pintar a área total deste cilindro, baseado nos dados fornecidos, seram necessárias:', quantidadeLata , 'latas custando um total de: R$', custoLata )


#a. A lata de tinta custa R$ 50,00
#b. Cada lata contém 5 litros
#c. Cada litro de tinta pinta 3 metros quadrados
#d. Entrada do programa: altura e raio do cilindro
#. Saída: valor em reais e quantidade de latas