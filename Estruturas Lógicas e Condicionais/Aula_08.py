"""
Função input() - função para receber dados do usuario
"""

nome = input("Qual eh o seu nome:")
idade = input("Qual a sua idade:")

print("Olá " + nome + " você tem " + idade + " anos")
print("Olá {0} você tem {1} anos".format(nome, idade))
print(f"Seu nome é: {nome} e sua idade é: {idade}")
