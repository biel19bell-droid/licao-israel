A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))

soma = A + B
subtracao = A - B
multiplicacao = A * B


if B != 0:
    divisao = A / B
else:
    divisao = "não é possível dividir por zero"

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)