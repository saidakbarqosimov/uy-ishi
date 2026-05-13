speed = {
    "Tesla": 250,
    "BMW": 240,
    "Mercedes": 260,
    "Audi": 230
}

saralangan = sorted(speed.items(), key=lambda x: x[1], reverse=True)

print("Tezlik bo'yicha saralash:")
for mashina, tezlik in saralangan:
    print(mashina, "-", tezlik, "km/s")
