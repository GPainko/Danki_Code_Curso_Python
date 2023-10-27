"""lista : Coleção ordenada, mutavel e que permite valores duplicados
tupla : coleção ordenada, imutavel e que permite valores duplicados
dicionarios : coleção noa ordenada, mutavel e que não permite valores duplicados"""

# chave-valor
dicio = {"chave1": "Gabriel", "chave2": 1992, "chave3 ": True}
print(dicio)

dicionario = {
    "nome": "Guilherme",
    "idade": 24,
    "nacionalidade": "Brasileiro"
}

print(dicionario)

print(dicionario["idade"])

print(dicionario.get("idade"))


dicionario["nacionalidade"] = "Japão"
print(dicionario)
