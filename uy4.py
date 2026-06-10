class BankHisob:
    def __init__(self, ism, balans=0):
        self.ism = ism
        self.balans = balans

    def deposit(self, summa):
        self.balans += summa

    def yechib_ol(self, summa):
        if self.balans >= summa:
            self.balans -= summa

    def hisob(self):
        return self.balans

mijoz = BankHisob("Alijon")
mijoz.deposit(1000)
mijoz.yechib_ol(400)
print(mijoz.hisob())
