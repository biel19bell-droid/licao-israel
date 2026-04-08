distancia = float(input("Digite a distância em metros: "))
tempo = float(input("Digite o tempo em segundos: "))

velocidade = (distancia * 1000) / (tempo * 60)

print("A velocidade é:", velocidade, "m/s")