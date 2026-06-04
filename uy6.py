def baholarni_guruhla(talabalar):
    guruhlangan = {} # Yangi bo'sh lug'at (dict) ochamiz
    
    # Lug'at ichidagi ism va baholarni bittama-bitta olamiz
    for ism, baho in talabalar.items():
        # Agar bu baho hali yangi lug'atimizda kalit sifatida bo'lmasa
        if baho not in guruhlangan:
            # Shu baho uchun bo'sh ro'yxat yaratamiz va ismni qo'shamiz
            guruhlangan[baho] = [ism]
        else:
            # Agar bu baho oldin ro'yxatga olingan bo'lsa, ro'yxatga ismni qo'shamiz
            guruhlangan[baho].append(ism)
            
    return guruhlangan

# Tekshirish
sinf = {'Ali': 5, 'Vali': 4, 'Gulnoza': 5}
print(baholarni_guruhla(sinf))
# Output: {5: ['Ali', 'Gulnoza'], 4: ['Vali']}
