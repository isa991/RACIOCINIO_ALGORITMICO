#Faça um algoritmo que calcule o consumo médio de um automóvel
#(medido em km/l), solicitando como entrada a distância total
#percorrida (KM) e o volume de combustível consumido para
#percorre-la (litros).

print('Para calcular o consumo médio do seu automóvel, insira as seguintes informações.')

distanciaTotal = int(input('Qual a distância que será percorrida? (em km) '))
volumeCombustivel = int(input('Qual o volume de combustível que deverá ser utilizado para correr tal distância? (em L)'))

consumoMedio = (distanciaTotal / volumeCombustivel)

print('O consumo médio do autómovel, baseado nas informações inseridas, será de:', consumoMedio, 'km/L.')