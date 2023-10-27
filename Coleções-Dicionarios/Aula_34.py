dicio = {"nome": "Guilherme", "ano": 2000, "valor_logico": True}
print(dicio)

dicio["nome"] = "pedro"
print(dicio)

dicio.update({"nome": "Luis"})
print(dicio)

dicio["idade"] = 20
print(dicio)

dicio.update({"pokemon": "gengar"})
print(dicio)
print(50 * "_")
for x in dicio:
    print(x)
print(50 * "_")
for x in dicio:
    print(x, dicio[x])
print(50 * "_")
for x in dicio.values():
    print(x)
print(50 * "_")
for x, y in dicio.items():
    print(x, y)
print(50 * "_")

dados = dicio.copy()
print(dados)

dados2 = dict(dicio)
print(dados2)

dicio["idade"] = 30
print(dicio)
print(50 * "_")
# função popotem elemina o ultimo item apenas da versão 3.7 e acima
dicio.popitem()  # nas outras versão(abaico da 3.7) essa função elimina um item aleatorio
print(dicio)

dicio.pop("valor_logico")
print(dicio)

del dicio["ano"]
print(dicio)

dicio.clear()
print(dicio)
