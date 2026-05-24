with open("tekst.txt", "r", encoding="utf-8") as file:
    matn = file.read()

yangi_matn = matn.title()

with open("tekst.txt", "w", encoding="utf-8") as file:
    file.write(yangi_matn)
