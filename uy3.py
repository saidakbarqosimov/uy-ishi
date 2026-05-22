from datetime import date

bugun = date.today()
bayram = date(bugun.year, 9, 1)

if bugun > bayram:
    bayram = date(bugun.year + 1, 9, 1)

qolgan_kun = (bayram - bugun).days
print(f"Keyingi Mustaqillik bayramiga {qolgan_kun} kun qoldi.")
