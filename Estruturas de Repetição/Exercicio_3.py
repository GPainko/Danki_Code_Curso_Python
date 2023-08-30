# Inicialização das variáveis
# Lê o primeiro valor e atribui a ambos maior e menor
maior = menor = int(input("Digite o 1º valor: "))

# Loop para ler os próximos 4 valores
for i in range(2, 6):
    valor = float(input(f"Digite o {i}º valor: "))
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor

# Mostrar os resultados
print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")
print(50 * "-")


# Soma 1
soma1 = 0
numerator1 = 3
denominator1 = 40
for _ in range(5):
    soma1 += numerator1 / denominator1
    numerator1 += 1
    denominator1 -= 1

# Soma 2
soma2 = 0
numerator2 = 480
for i in range(20):
    soma2 += numerator2 / (2 + i)
    numerator2 -= 5

# Soma 3
soma3 = 0
numerator3 = 1
denominator3 = 2
for i in range(15):
    soma3 += numerator3 / denominator3
    numerator3 *= 2
    denominator3 += 2

# Mostrar os resultados
print("Soma 1:", soma1)
print("Soma 2:", soma2)
print("Soma 3:", soma3)
