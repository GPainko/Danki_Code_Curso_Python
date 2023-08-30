# como descobrir se o numero é impar ou par

# 0,2,4,6,8,10,12,14,...

# 0/2 , 2/2 , 4/2 , ... divisao inteira |resto da divisao = 0

numero = int(input("insire o numero que deseja saber se é par: "))

print(7 * "-")
if (numero % 2) == 0:
    print(f"{numero} é par")
else:
    print(f"{numero} é impar")
print(40 * "-")
