A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if B != 0:
    resultado = (A / B) ** 2
    print("O resultado é:", resultado)
else:
    print("Não é possível dividir por zero")