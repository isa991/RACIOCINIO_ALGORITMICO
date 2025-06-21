'''
8. Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um
número que ele gostaria de pesquisar neste vetor, caso o número exista no vetor, mostre em qual(is)
posição(ões) ele foi encontrado e quantas ocorrências foram detectadas.
'''

print('Insira 10 posições inteiras para um vetor.')
indice = 0
vetor = []

for i in range(0, 10):
    valor = int(input(f'Insira a {i+1}° posição inteira do vetor: '))
    vetor.append(valor)

pesquisa = int(input('Insira o número inteiro que deseja pesquisar dentro do vetor: '))
ocorrencia = 0
pos = []

for i in range (len(vetor)):
    if  vetor[i] == pesquisa:
        ocorrencia += 1
        pos.append(i)

encontrou = False
for i in range (len(vetor)):
    if pesquisa == vetor[i]:
        encontrou = True
        print('O número ', pesquisa, 'pesquisado existe dentro do vetor e está localizado inicialmente na posição: ', indice)
    i += 1

if ocorrencia > 0:
    print('A ocorrência do número foi de: ', ocorrencia, 'vez(es) na(s) posição(ões): ', pos)

if not encontrou:
        print('O número inteiro pesquisado não existe dentro do vetor.')