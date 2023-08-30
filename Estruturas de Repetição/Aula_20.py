# como achar o fatorial de um numero

fatorial = 1
numero = int(input("digite o valor desejado: "))

if numero < 0:
    print("Não existe fatorial de numero negativo")
elif numero == 0:
    print(f"o fatorial de {numero} eh 1")
else:
    for x in range(1, numero + 1):
        fatorial = fatorial * x
        print(fatorial)
print(fatorial)
