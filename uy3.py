books = [
    ("O'tkan kunlar", "Roman"),
    ("Mehrobdan chayon", "Roman"),
    ("Shum bola", "Povest"),
    ("Alkimyogar", "Roman"),
    ("Boy va kambag'al", "Hikoya"),
    ("Urush va tinchlik", "Roman"),
    ("Kecha va kunduz", "Roman"),
    ("Yulduzli tunlar", "Povest"),
    ("Qorako'z Majnun", "Hikoya"),
    ("Qalb ko'zi", "Hikoya")
]

guruhlangan_kitoblar = {}

for nomi, janri in books:
    if janri not in guruhlangan_kitoblar:
        guruhlangan_kitoblar[janri] = []
    guruhlangan_kitoblar[janri].append(nomi)

print(guruhlangan_kitoblar)
