# descobrir se um numero é primo

print(30 * "_")

numero = int(input("insira um numero para ver se é primo:"))

if numero > 1:
    for x in range(2, numero):
        if (numero % x) == 0:
            print("esse não é um numero primo")
            break
    else:
        print("esse numeo é um numero primo")
else:
    print("deslige seu PC se nao ele vai explodir")
