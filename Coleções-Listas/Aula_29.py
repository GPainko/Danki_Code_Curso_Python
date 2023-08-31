#           0       1        2     -> 3 elementos
lista1 = ["banana", "Maça", "laranja", "Abacate",]
#         0  1  2  3  4  5 -> 6 elementos
lista2 = [1, 2, 3, 4, 5, 6]
#          0    1   2     3    4 -> 5 elementos
lista3 = [1.2, 2.3, 3.4, 4.5, 6.7]
#          0     1 -> 2 elementos
lista4 = [True, False]
#           0        1    2   3 -> 4 elementos
lista5 = ["banana", True, 2, 3.4]

lista6 = lista2 + lista3
lista6.extend(lista2)
print(lista6)

for x in lista3:
    lista6.append(x)
print(lista6)

lista7 = lista6
print(lista7)
print(100 * "-")
lista7.append(8)
print(lista6)
print(lista7)

lista8 = lista7.copy()
print(lista8)
print(100 * "-")
lista8.append(200)
print(lista6)
print(lista7)
print(lista8)
