def birlarni_sana(matritsa):
    natija = [] # Har bir qatordagi 1 lar sonini yig'ish uchun ro'yxat
    
    # Matritsani qatorma-qator aylanib chiqamiz
    for qator in matritsa:
        # count() funksiyasi qatorda nechta 1 borligini sanaydi
        birlar_soni = qator.count(1)
        # Sanog'ini ro'yxatga qo'shamiz
        natija.append(birlar_soni)
        
    return natija

# Tekshirish
matritsa = [[1, 0, 1], [1, 1, 0], [0, 0, 1]]
print(birlarni_sana(matritsa))
# Output: [2, 2, 1]
