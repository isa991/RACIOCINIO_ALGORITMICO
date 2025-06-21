'''
Considerando a mesma tabela da questão anterior, desenvolva um programa que permita ao usuário informar várias cidades
em sequência, até inserir um código finalizador. Mostre então as cidades que compõem o roteiro fornecido,
a distância de cada percurso intermediário e a distância total do roteiro fornecido.
'''

cidades = ["Curitiba", "Florianópolis", "Porto Alegre", "São Paulo", "Rio de Janeiro"]

print("Códigos das cidades disponíveis:")
for i, nome in enumerate(cidades):
    print(f"{nome} [{i}]")

percurso = []
print("\nDigite os códigos das cidades de seu roteiro. Digite -1 para finalizar.")
while True:
    codigo = int(input("Cidade: "))
    if codigo == -1:
        if len(percurso) < 2:
            print("Informe ao menos duas cidades.")
            continue
        break
    elif 0 <= codigo < len(cidades):
        percurso.append(codigo)
    else:
        print("O código informado é inválido. Tente novamente.")

m = [
    [" - ", 310, 716, 408, 852],
    [310, " - ", 470, 705, 1144],
    [716, 470, " - ", 1119, 1553],
    [408, 705, 1119, " - ", 429],
    [852, 1144, 1553, 429, " - "]
]

vel = int(input("\nQual será a velocidade média da viagem? (km/h): "))

print("\nROTEIRO DA VIAGEM: ")
distancia_tot = 0
tmp_tot_h = 0

for i in range(len(percurso) - 1):
    origem = percurso[i]
    destino = percurso[i + 1]
    distancia = m[origem][destino]

    if isinstance(distancia, str):
        print(f"{cidades[origem]} -> {cidades[destino]}: Foram informadas como origem e destino a mesma cidade (0 km, 0 minutos).")
        continue

    tmp_h = distancia / vel
    h = int(tmp_h)
    mnts = round((tmp_h - h) * 60)

    print(f"{cidades[origem]} --> {cidades[destino]}: {distancia} km, tempo estimado: ", end="")
    if h > 0 and mnts > 0:
        print(f"{h} horas e {mnts} minutos.")
    elif h > 0:
        print(f"{h} horas.")
    else:
        print(f"{mnts} minutos.")

    distancia_tot += distancia
    tmp_tot_h += tmp_h

h_tot = int(tmp_tot_h)
mnts_tot = round((tmp_tot_h - h_tot) * 60)

print("\nRESUMO DA VIAGEM: ")
print(f"A distância total a ser percorrida é: {distancia_tot} km")
print("O tempo total estimado é de: ", end="")
if h_tot > 0 and mnts_tot > 0:
    print(f"{h_tot} horas e {mnts_tot} minutos.")
elif h_tot > 0:
    print(f"{h_tot} horas.")
else:
    print(f"{mnts_tot} minutos.")