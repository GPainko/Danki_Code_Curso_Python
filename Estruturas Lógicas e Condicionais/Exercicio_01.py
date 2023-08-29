"""

Exercicíos - Python

Observação: Todos os exercicios devem utilizar a função input,
de modo que o usuario possa determinar os dados de entrada.

"""

# 1 - área de um retnagulo

base = int(input("Qual a base do retangulo: "))
altura = int(input("Qual a altura do retangulo: "))
area = base * altura
print(f"a area é {area}")

# 2 - área de um quadrado

lado_quadrado = int(input("Qual o valor dos lado do Quadrado; "))
area_quadrado = lado_quadrado*lado_quadrado
print(f"a area do quadrado é {area_quadrado}")

# 3 - se o produto que você quer avaliar custa(???)
# reais qual será o valor do mesmo com desconto de (??)%.

valor_produto = float(input("Informe o valor do produto: "))
desconto_produto = int(input("Informe o desconto: "))
desconto = float(desconto_produto/100)
valor_com_desconto = valor_produto - (valor_produto * desconto)
print(f"O valor com desconto é {valor_com_desconto} ")

# 4 - área do circulo

pi = float(input("informe o valor de pi que seja usar: "))
raio = int(input("informe o valor do raio: "))
area_circulo = pi * raio ** 2
print(f"o valor da area do circulo é {area_circulo}")

# 5 - conversão de reais para dolar
valor_real = float(input("informe o valor que deseja converte para dolar: "))
valor_dolar = valor_real/4.85
print(f"o valor em dolar é {valor_dolar}")
# 6 - conversão de dolar para reais.
dolar_valor = float(input("informe o valor que deseja converte para reais: "))
real_valor = dolar_valor * 4.85
print(f"o valor em reais é {real_valor}")
