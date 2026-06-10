class KitobOb:
    def __init__(self, nomi, muallif):
        self.nomi, self.muallif = nomi, muallif

class Kutubxona:
    def __init__(self):
        self.kitoblar = []

    def kitob_qoshish(self, kitob):
        self.kitoblar.append(kitob)

    def qidirish(self, nom):
        for k in self.kitoblar:
            if k.nomi.lower() == nom.lower():
                return f"{k.nomi}, {k.muallif}"
        return "Topilmadi"

k1 = KitobOb("Sariq devni minib", "X.To'xtaboyev")
k2 = KitobOb("Dunyoning ishlari", "O'.Hoshimov")

kutubxona = Kutubxona()
kutubxona.kitob_qoshish(k1)
kutubxona.kitob_qoshish(k2)
print(kutubxona.qidirish("Dunyoning ishlari"))
