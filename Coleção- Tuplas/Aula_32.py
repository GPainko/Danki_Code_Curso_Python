tupla = ("item1",)

tupla2 = ("item1", "item2")

tupla3 = ("item1", "item2", "item3")

tupla = tupla + tupla2 * 3
print(tupla)

for x in tupla:
    print(x)
for x in range(len(tupla)):
    print(x, "-", tupla[x])

(x, y, z) = tupla3

print(x)
print(y)
print(z)

(w, *t) = tupla3

print(w)
print(t)


