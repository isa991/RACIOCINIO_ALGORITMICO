'''
A distância rodoviária entre algumas capitais brasileiras está disponível na tabela abaixo.
Para consultar a distância basta cruzar as cidades origem e destino, ou seja, a distância entre Curitiba e São Paulo é de 408 km.
Construa um programa que inicialize uma matriz contendo as distâncias apresentadas na tabela acima e que então informe ao usuário
o tempo necessário para percorrer duas cidades por ele fornecidas.
'''

cidades = ["Curitiba [0]", "Florianópolis [1]", "Porto Alegre [2]", "São Paulo [3]", "Rio de Janeiro [4]"]
print(f"{cidades}\n")

cid_1 = int(input("Informe a cidade da qual você vai sair: "))
cid_2 = int(input("Informe a cidade para qual você vai: "))

m = [
    [" - ", 310, 716, 408, 852],
    [310, " - ", 470, 705, 1144],
    [716, 470, " - ", 1119, 1553],
    [408, 705, 1119, " - ", 429],
    [852, 1144, 1553, 429, " - "]
]

print("\nTABELA DE DISTÂNCIAS (km):")
for i in range(len(m)):
    for j in range(len(m[0])):
        print(f"{m[i][j]:>4}", end=' | ')
    print()

vel = int(input("\nInforme em qual velocidade você vai viajar (km/h): "))

distancia = m[cid_1][cid_2]

if isinstance(distancia, str):
    print("Você informou a mesma cidade como origem e destino.")
else:
    tmp_h_dec = distancia / vel
    h = int(tmp_h_dec)
    mnts = round((tmp_h_dec - h) * 60)

    print(f"\nVocê está viajando de {cidades[cid_1]} até {cidades[cid_2]}, à uma velocidade de {vel}km/h.")
    print(f"O percurso possui {distancia} km de distância.")

    if h > 0 and mnts > 0:
        print(f"Sua viagem vai levar cerca de {h} horas e {mnts} minutos.")
    elif h > 0:
        print(f"Sua viagem vai levar cerca de {h} horas.")
    else:
        print(f"Sua viagem vai levar cerca de {mnts} minutos.")