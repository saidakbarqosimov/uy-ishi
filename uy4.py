professions = {
    "Bill Gates": "Dasturchi",
    "Cristiano Ronaldo": "Futbolchi",
    "Elon Musk": "Tadbirkor",
    "Messi": "Futbolchi"
}

ism = input("Ism kiriting: ")

ism_kichik = ism.strip().lower()

topildi = False

for kalit, qiymat in professions.items():
    if kalit.lower() == ism_kichik: 
        print(kalit, "ning kasbi:", qiymat)
        topildi = True
        break 

if topildi == False:
    print("Kechirasiz, bunday shaxs ro'yxatda yo'q.")
