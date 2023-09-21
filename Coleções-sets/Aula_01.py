"""
set: Coleção não ordenada, imutavel e que não permite valores duplicados 
sets tambem conhecidos como conjuntos
"""

conjunto = {3, True, 3.7, "são paulo"}
print(type(conjunto))
print(conjunto)

tupla = (3, 7, 9, 8, 5)
conjunto1 = set(tupla)
print(conjunto1)
print(type(conjunto1))

for x in conjunto1:
    print(x)

print(6 in conjunto1)
print(3 in conjunto1)

set1 = {"item1", "item2", "item3"}
print(set1)
set1.add("item4")
print(set1)

set1.remove("item2")
set1.discard("item1")
set1.pop()
set1.clear()
print(set1)
