#       0123456
nome = "chicago"
nome2 = "queens"
print(nome, end=" ")
print(nome2)
for x in range(10, -1, -1):
    print(x, end=" ")
print(100*"-")
for y in nome:
    print(y, end=" ")
print(100*"-")
x = 5
y = 0
x, y = y, x
print(x)
print(y)
