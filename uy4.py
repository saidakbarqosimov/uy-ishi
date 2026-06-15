class Taqvim:
    def hijriyga(self, g_yil):
        # Grigoriyandan Hijriyga o'tkazish formulasi
        h_yil = int((g_yil - 622) * (33 / 32))
        return h_yil

    def grigoriyanga(self, h_yil):
        # Hijriydan Grigoriyanga o'tkazish formulasi
        g_yil = int(h_yil * (32 / 33) + 622)
        return g_yil

    def kabisami(self, yil):
        # 4 ga bo'linsa va 100 ga bo'linmasa, Yoki 400 ga bo'linsa kabisa
        if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
            return True
        return False

# Tekshirish
tq = Taqvim()
print(f"2024-yil hijriyda: {tq.hijriyga(2024)}")     # 1445 yoki 1446
print(f"1445-yil grigoriyanda: {tq.grigoriyanga(1445)}") # 2023 yoki 2024
print(f"2024 kabisami?: {tq.kabisami(2024)}")         # True
