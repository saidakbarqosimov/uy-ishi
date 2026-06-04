def raqamni_top(kitob, ism):
    # dict tarkibidan kalit (ism) borligini tekshiramiz
    if ism in kitob:
        return kitob[ism] # Agar ism bo'lsa, uning raqamini qaytaramiz
    else:
        return "Topilmadi" # Agar ism bo'lmasa, matn qaytadi

# Tekshirish
kitob = {'Ali': '998901234567', 'Gulnoza': '998935678901'}
print(raqamni_top(kitob, 'Ali'))        # Output: 998901234567
print(raqamni_top(kitob, 'Sardor'))     # Output: Topilmadi
