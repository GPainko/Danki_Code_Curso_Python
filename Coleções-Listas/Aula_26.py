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

print(lista6)
# tamanho da lista
print(len(lista6))
# somatorio da lista
print(sum(lista6))
# valor maximo da lista
print(max(lista6))
# valor minimo da lista
print(min(lista6))

nome = "Curso de Python"
valor = range(10)

print(nome)
print(valor)

lista7 = list(range(10))
print(lista7)

lista8 = list("Curso de Python")
print(lista8)

elemento = 8

if elemento in lista7:
    print("este elemento esta dento da lista")
