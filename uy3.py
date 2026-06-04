def arzon_narxni_top(mahsulotlar):
    natija = [] # Natijalarni saqlash uchun bo'sh ro'yxat
    
    for mahsulot in mahsulotlar:
        nomi = mahsulot[0]   # Mahsulot nomi
        narxlar = mahsulot[1] # Narxlar ro'yxati
        
        # min() funksiyasi ro'yxat ichidagi eng kichik sonni topib beradi
        eng_arzon = min(narxlar)
        
        # Nomi va eng arzon narxni yangi ro'yxat qilib qo'shamiz
        natija.append([nomi, eng_arzon])
        
    return natija

# Tekshirish
ombor = [['Olma', [12000, 11000, 11500]], ['Banan', [13000, 12500]]]
print(arzon_narxni_top(ombor))
# Output: [['Olma', 11000], ['Banan', 12500]]
