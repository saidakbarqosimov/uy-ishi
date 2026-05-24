search_word = input("So'z kiriting: ").lower()

with open("matn.txt", "r", encoding="utf-8") as file:
    content = file.read().lower()
    
    if content.find(search_word) != -1:
        print("Siz kiritgan so'z faylda bor.")
    else:
        print("Siz kiritgan so'z faylda yo'q.")
