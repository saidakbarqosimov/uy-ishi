def bank_kalkulyatori(depozit, foiz, yil):
    yakuniy_summa = depozit + (depozit * (foiz / 100) * yil)
    return int(yakuniy_summa)

natija = bank_kalkulyatori(depozit=10000, foiz=24, yil=3)
print(natija)
