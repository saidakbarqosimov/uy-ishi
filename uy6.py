class Kurs:
    def __init__(self, nomi, davomiylik):
        self.nomi = nomi
        self.davomiylik = davomiylik
        self.talabalar = []

    def talaba_qoshish(self, ism):
        self.talabalar.append(ism)

    def talabalar_soni(self):
        return len(self.talabalar)

python_kurs = Kurs("Python", "4 oy")
python_kurs.talaba_qoshish("Anvar")
python_kurs.talaba_qoshish("Sardor")
python_kurs.talaba_qoshish("Nodira")
print(python_kurs.talabalar_soni())
