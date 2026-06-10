class Avtomobil:
    def __init__(self, model, yil, tezlik=0):
        self.model = model
        self.yil = yil
        self.tezlik = tezlik

    def tezlashtir(self):
        self.tezlik += 10

    def sekinlashtir(self):
        self.tezlik -= 10

    def info(self):
        print(f"{self.model}, {self.yil}, {self.tezlik} km/s")

mashina = Avtomobil("Gentra", 2024, 60)
mashina.tezlashtir()
mashina.tezlashtir()
mashina.tezlashtir()
mashina.sekinlashtir()
mashina.info()
