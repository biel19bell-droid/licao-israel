A = int(input("Digite os votos do candidato A: "))
B = int(input("Digite os votos do candidato B: "))
C = int(input("Digite os votos do candidato C: "))
nulos = int(input("Digite os votos nulos: "))
brancos = int(input("Digite os votos em branco: "))

total = A + B + C + nulos + brancos

perc_validos = ((A + B + C) / total) * 100
perc_A = (A / total) * 100
perc_B = (B / total) * 100
perc_C = (C / total) * 100
perc_nulos = (nulos / total) * 100
perc_brancos = (brancos / total) * 100

print("Total de eleitores:", total)
print("Percentual de votos válidos:", perc_validos, "%")
print("Percentual candidato A:", perc_A, "%")
print("Percentual candidato B:", perc_B, "%")
print("Percentual candidato C:", perc_C, "%")
print("Percentual votos nulos:", perc_nulos, "%")
print("Percentual votos em branco:", perc_brancos, "%")