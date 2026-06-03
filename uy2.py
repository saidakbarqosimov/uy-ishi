def ortacha_narx(mahsulotlar):
    for mahsulot, narxlar in mahsulotlar.items():
        ortacha = sum(narxlar) // len(narxlar)
        print(f"{mahsulot}: {ortacha}")

input_data = {
    "olma": [13000, 14000, 15000],
    "anor": [19000, 22000, 24000, 15000],
    "gilos": [6000, 9000, 5000, 4000],
    "banan": [30000, 28000]
}

ortacha_narx(input_data)
