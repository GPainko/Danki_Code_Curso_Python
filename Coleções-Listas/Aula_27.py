#           0       1        2     -> 3 elementos
lista1 = ["banana", "maça", "laranja"]
#         0  1  2  3  4  5 -> 6 elementos
lista2 = [1, 2, 3, 4, 5, 6]
#          0    1   2     3    4 -> 5 elementos
lista3 = [1.2, 2.3, 3.4, 4.5, 6.7]
#          0     1 -> 2 elementos
lista4 = [True, False]
#           0        1    2   3 -> 4 elementos
lista5 = ["banana", True, 2, 3.4]

lista6 = lista2 + lista3

print(lista3)
print(type(lista3))
print(lista3[2])

# modificação de apenas um valor na lista
lista3[2] = 7.2
print(lista3)
# modificação dos itens do indice i ate o indice 3
lista3[1:4] = [2.6, 8.3, 12.3]
print(lista3)
# modificação dos itens do indice i ate o indice 2
lista3[1:3] = [2.2, 4.6]
print(lista3)

print(lista1)

for x in lista1:
    print(x)

print(len(lista1))

for y in range(len(lista1)):
    print(y, "-", lista1[y])

texto = "bergamota, abacaxi"
lista9 = list(texto)
print(lista9)

texto = texto.split(',')
print(texto)

lista1.extend(["abacaxi", "abacate"])
lista1.append("manga")
lista1.insert(1, "uva")
print(lista1)

for y in range(len(lista1)):
    print(y, "-", lista1[y])
