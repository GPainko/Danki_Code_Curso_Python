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

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)

print(type(lista1))
print(type(lista2))
print(type(lista3))
print(type(lista4))
print(type(lista5))

print(lista1[2])
print(lista2[5])
print(lista3[4])
print(lista4[0])
print(lista5[1])


print(lista1[-2])
print(lista2[-5])
print(lista3[-4])
print(lista4[0])
print(lista5[-1])

print(lista5[::])
print(lista5[1:])  # retorna do index que destacamos ate o fim da lista
print(lista5[2:])  # retorna do index que destacamos ate o fim da lista
print(lista5[:3])  # retorna do index do começo  ate o index -1
print(lista5[1:3])  # retorna do index destacado ate index -1
print(lista5[0:4:2])
