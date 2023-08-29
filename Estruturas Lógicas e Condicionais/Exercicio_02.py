# 1 -implementar um programa
# que receba a idade de uma pessoa
# e imprima mensagem de acordo com os criterios
# menor de 16 anos: menor
# entre 16 e 18 anos: emancipado
# maior de 18 anos:maior

idade = int(input("informe sua idade:"))

if idade < 16:
    print("menor")
elif idade > 18:
    print("maior")
else:
    print("emancipado")

"""
2 - Implementar um programa que receba a idade 
de um nador e imprima na tela a sua categoria
de acordo com as regras

categoria  | idade

infantil A | 5 - 7 anos
infantil B | 8 - 10 anos
Juvenil  A | 11 - 13 anos
Juvenil  B ! 14 - 17 anos
"""

idade_nadador = int(input("informe a idade do nadador:"))

if 5 <= idade_nadador <= 7:
    print("infantil A")
elif 8 <= idade_nadador <= 10:
    print("infantil B")
elif 11 <= idade_nadador <= 13:
    print("juvenil A")
elif 14 <= idade_nadador <= 17:
    print("juvenil B")
else:
    print("o nadador não possue idade adequada")
