a = 5
b = 3
c = 2

if b > a:
    print("b é maior que a")
print("codigo fora do if")

# operador ternario|expressoes condicionais
print("B") if b > a else print("A")

if a > b:
    print("A")
    if a > c:
        print("A é maior que b e c")
