'''
Desenvolva um programa que leia um vetor de 20 posições inteiras e o coloque em ordem crescente,
utilizando a seguinte estratégia de ordenação:
• selecione o elemento do vetor de 20 posições que apresenta o menor valor;
• troque este elemento pelo primeiro;
• repita estas operações, envolvendo agora apenas os 19 elementos restantes (trocando o de
menor valor com a segunda posição), depois os 18 elementos (trocando o de menor valor com a
terceira posição), depois os 17, 16 e assim por diante, até restar um único elemento, o maior
deles.
Observação: este método de ordenação é conhecido como “Seleção Direta”
'''

vetor = []

for i in range (1,21):
    num = int(input(f'Insira o {i}° número inteiro do vetor: '))
    vetor.append(num)

print('Vetor original: ', vetor)
vetor2 = []

while len(vetor):
    menor = min(vetor)
    vetor.remove(menor)
    vetor2.append(menor)

print('Vetor em ordem decrescente: ',vetor2)