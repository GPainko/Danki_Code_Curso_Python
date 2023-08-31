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
print(lista6)

lista6.pop()
print(lista6)

lista6.remove(2.3)
print(lista6)

lista6.pop(3)
print(lista6)

del lista6[0]
print(lista6)

lista6.reverse()
print(lista6)

lista6.sort()
print(lista6)

lista6.sort(reverse=True)
print(lista6)

lista6.clear()
print(lista6)

print(lista1)
lista1.sort(key=str.lower)
print(lista1)
