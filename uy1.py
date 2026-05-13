cars = {
    "Malibu": 35000,
    "Spark": 12000,
    "Cobalt": 18000,
    "Tracker": 28000
}

narxlar = cars.values()

eng_qimmat_narx = max(narxlar)
eng_arzon_narx = min(narxlar)

ortacha_narx = sum(narxlar) / len(cars)

print("Eng qimmat narx:", eng_qimmat_narx)
print("Eng arzon narx:", eng_arzon_narx)
print("O'rtacha narx:", ortacha_narx)

