import math

class Uchburchak:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimetr(self):
        return self.a + self.b + self.c

    def maydon(self):
        p = self.perimetr() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

shakl = Uchburchak(3, 4, 5)
print(shakl.perimetr())
print(shakl.maydon())
