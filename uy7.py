def mahsulot_sarala(mahsulotlar):
    saralanganlar = [] # Shartga mos kelgan mahsulotlar uchun ro'yxat
    
    # Har bir mahsulot (dict) ustida sikl yuritamiz
    for mahsulot in mahsulotlar:
        # Shartni tekshiramiz: narxi 10000 dan kichik VA turi "ichimlik" bo'lishi kerak
        if mahsulot['narx'] < 10000 and mahsulot['tur'] == 'ichimlik':
            # Shart bajarilsa, mahsulotni ro'yxatga qo'shamiz
            saralanganlar.append(mahsulot)
            
    return saralanganlar

# Tekshirish
ruyxat = [
  {'nom': 'Cola', 'narx': 9000, 'tur': 'ichimlik'},
  {'nom': 'Non', 'narx': 3000, 'tur': 'ovqat'},
  {'nom': 'Suv', 'narx': 5000, 'tur': 'ichimlik'}
]
print(mahsulot_sarala(ruyxat))
# Output: [{'nom': 'Cola', 'narx': 9000, 'tur': 'ichimlik'}, {'nom': 'Suv', 'narx': 5000, 'tur': 'ichimlik'}]
