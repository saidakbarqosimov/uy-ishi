from datetime import date

yil = int(input("Yil: "))
oy = int(input("Oy: "))
kun = int(input("Kun: "))

tugilgan_kun = date(yil, oy, kun)
bugun = date.today()
farq = bugun - tugilgan_kun

print(f"{farq.days} kun o'tdi")
