
valores_bondadosos = {
    "Pelosos": 1,
    "Sureños buenos": 2,
    "Enanos": 3,
    "Númenóreanos": 4,
    "Elfos": 5
}

valores_malvados = {
    "Sureños malos": 2,
    "Orcos": 2,
    "Goblins": 2,
    "Huargos": 3,
    "Trolls": 5
}


def calcular_fuerza(ejercito, valores):
    fuerza_total = 0
    for raza, cantidad in ejercito.items():
        fuerza_total += valores[raza] * cantidad
    return fuerza_total


ejercito_bondadoso = {
    "Pelosos": 3,
    "Elfos": 1
}

ejercito_malvado = {
    "Orcos": 1,
    "Trolls": 1
}


fuerza_bondadosa = calcular_fuerza(ejercito_bondadoso, valores_bondadosos)
fuerza_malvada = calcular_fuerza(ejercito_malvado, valores_malvados)


if fuerza_bondadosa > fuerza_malvada:
    resultado = "El bien gana"
elif fuerza_bondadosa < fuerza_malvada:
    resultado = "El mal gana"
else:
    resultado = "Empate"


print(f"Fuerza del bien: {fuerza_bondadosa}")
print(f"Fuerza del mal: {fuerza_malvada}")
print(resultado)
