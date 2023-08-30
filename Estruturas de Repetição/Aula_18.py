"""
do while
código para adivinha um numero
"""

palpite = 0
numero = 9

while True:
    print("Adivinhe qual é o numero correto !")
    palpite = int(input("Qual seu palpite: "))
    if palpite == numero:
        print(f"Você acertou o numero é {numero}")
        break
    else:
        print("Você errou, tente novamente")
else:
    print("erro!!!")
