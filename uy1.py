class Mahsulot:
    def __init__(self, nom, narx, miqdor):
        self.nom = nom
        self.narx = narx
        self.miqdor = miqdor

    def sotib_ol(self, miqdor):
        if self.miqdor >= miqdor:
            self.miqdor -= miqdor

    def qolgan_miqdor(self):
        return self.miqdor

olma = Mahsulot("Olma", 12000, 50)
olma.sotib_ol(10)
olma.sotib_ol(5)
print(olma.qolgan_miqdor())
