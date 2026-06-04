def ortacha_baho_hisobla(talabalar):
    natija = [] # Yangi ro'yxat ochamiz
    
    # Har bir talabaning ma'lumotini bittalab aylanib chiqamiz
    for talaba in talabalar:
        ism = talaba[0]       # Talabaning ismi ro'yxatning 0-indeksida
        baholar = talaba[1]   # Baholari esa 1-indeksida bo'ladi
        
        # O'rtacha bahoni topish formula: yig'indi / soni
        ortacha = sum(baholar) / len(baholar)
        
        # O'rtacha bahoni verguldan keyin 2 ta raqamgacha yaxlitlaymiz
        ortacha = round(ortacha, 2)
        
        # Ism va o'rtacha bahoni yangi ro'yxat ko'rinishida qo'shamiz
        natija.append([ism, ortacha])
        
    return natija

# Tekshirish
talabalar_ruyxati = [['Ali', [5, 4, 3]], ['Gulnoza', [4, 4, 5]]]
print(ortacha_baho_hisobla(talabalar_ruyxati)) 
# Output: [['Ali', 4.0], ['Gulnoza', 4.33]]
