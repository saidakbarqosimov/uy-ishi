class Kitob:
    def __init__(self, nomi, muallif, sahifa_soni):
        self.nomi = nomi
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni

    def qisqacha(self):
        return f"'{self.nomi}', {self.muallif}"

    def katta_kitobmi(self):
        return self.sahifa_soni > 300

kitob = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 400)
print(kitob.qisqacha())
print(kitob.katta_kitobmi())
