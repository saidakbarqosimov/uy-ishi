def email_tekshir(email):
    # Agar email ichida '@' belgisi umuman bo'lmasa, xato deb qaytaramiz
    if '@' not in email:
        return False
        
    # Emailni '@' belgisi orqali ikkita qismga ajratamiz (chap va o'ng tomon)
    qismlar = email.split('@')
    
    # split() funksiyasi ruxsat berilganidan ko'p ajratib yubormasligi va
    # '@' belgisidan oldin matn borligini tekshiramiz
    if len(qismlar) != 2 or qismlar[0] == "":
        return False
        
    # Email tarkibida ruxsat berilgan belgilarni aniqlab olamiz
    ruxsat_etilmaganlar = False
    
    # Email ichidagi har bir belgini bittalab tekshiramiz
    for belgi in email:
        # Belgi harf, raqam yoki ruxsat berilgan belgilar ekanini tekshiramiz
        if not (belgi.isalnum() or belgi in ['_', '.', '@']):
            ruxsat_etilmaganlar = True
            
    # Agar taqiqlangan belgi topilsa False, hammasi to'g'ri bo'lsa True qaytadi
    if ruxsat_etilmaganlar:
        return False
    else:
        return True

# Tekshirish (Input/Output)
print(email_tekshir("john@gmail.com"))    # True
print(email_tekshir("@lily.mail.ru"))    # False
print(email_tekshir("ali.hotmail.ru"))   # False
