import os

def tozalash():
    os.system("cls" if os.name == "nt" else "clear")

def son_kirit(matn):
    """Faqat butun son kiritishni majburlaydigan yordamchi funksiya"""
    while True:
        try:
            return int(input(matn))
        except ValueError:
            print("❌ Xato! Faqat son kiriting!")

# ================= 2-MASALA: RESTORAN =================
class Restoran:
    def __init__(self, vaqti: str, menyu: list):
        self.vaqti = vaqti
        self.menyu = menyu

    def add_food(self):
        tozalash()
        print("🍔 YANGI TAOM QO'SHISH 🍔")
        while True:
            ovqat = input("Taom nomini kiriting (chiqish uchun '0'): ").strip()
            if ovqat == "0":
                break
            if ovqat in self.menyu:
                print(f"⚠️ {ovqat} menyuda allaqachon bor!")
            elif ovqat == "":
                print("⚠️ Taom nomi bo'sh bo'lishi mumkin emas!")
            else:
                self.menyu.append(ovqat)
                print(f"✅ {ovqat} menyuga muvaffaqiyatli qo'shildi!")

    def get_work_time(self):
        tozalash()
        print("🕒 ISH VAQTI REJIMI 🕒")
        print(f"Restoranimiz ish vaqti: {self.vaqti}")
        input("\nDavom etish uchun [Enter] bosing...")

# ================= 3-MASALA: USER =================
class User:
    def __init__(self, name: str, uname: str):
        self.name = name
        self.uname = uname
        self.followers = ["ali_01", "valijon", "madina_r"] # Namuna uchun boshlang'ich obunachilar
        self.following = []

    def follow(self):
        tozalash()
        print("➕ KIMGANDIR OBUNA BO'LISH ➕")
        kimga = input("Obuna bo'lmoqchi bo'lgan odam username'ini yozing: ").strip()
        if kimga == "":
            print("⚠️ Username bo'sh bo'lishi mumkin emas!")
        elif kimga in self.following:
            print("⚠️ Siz unga allaqachon obuna bo'lgansiz!")
        else:
            self.following.append(kimga)
            print(f"✅ Siz {kimga}ga muvaffaqiyatli obuna bo'ldingiz!")
        input("\n[Enter] bosing...")

    def unfollow(self):
        tozalash()
        print("➖ OBUNANI BEKOR QILISH ➖")
        if not self.following:
            print("Siz hali hech kimga obuna bo'lmagansiz!")
            input("\n[Enter] bosing...")
            return
        
        print("Siz obuna bo'lganlar:", ", ".join(self.following))
        kimdan = input("Kimdan obunani o'chirmoqchisiz?: ").strip()
        if kimdan in self.following:
            self.following.remove(kimdan)
            print(f"❌ {kimdan} obunasi o'chirildi!")
        else:
            print("⚠️ Siz bu foydalanuvchiga obuna bo'lmagansiz!")
        input("\n[Enter] bosing...")

    def remove_follower(self):
        tozalash()
        print("🗑 OBUNACHINI O'CHIRISH 🗑")
        if not self.followers:
            print("Sizda obunachilar yo'q!")
            input("\n[Enter] bosing...")
            return

        print("Sizning obunachilaringiz:", ", ".join(self.followers))
        kimni = input("Qaysi obunachini o'chirib tashlamoqchisiz?: ").strip()
        if kimni in self.followers:
            self.followers.remove(kimni)
            print(f"🗑 {kimni} sizning obunachilaringiz ro'yxatidan o'chirildi!")
        else:
            print("⚠️ Bunday obunachi sizda topilmadi!")
        input("\n[Enter] bosing...")

# ================= 4-MASALA: PHONE =================
class Phone:
    def __init__(self, brand: str, model: str, narx: int, yili: int):
        self.brand = brand
        self.model = model
        self.narx = narx
        self.yili = yili

    def update_price(self):
        tozalash()
        print("💰 TELEFON NARXINI YANGILASH 💰")
        print(f"Hozirgi narx: ${self.narx}")
        print("1. Narxni foizda oshirish (%)")
        print("2. Narxni yangi qiymatga o'zgartirish ($)")
        print("0. Orqaga")
        
        tanlov = son_kirit("Tanlang >>> ")
        if tanlov == 1:
            foiz = son_kirit("Qancha foizga oshsin?: ")
            self.narx += int(self.narx * (foiz / 100))
            print(f"✅ Narx {foiz}% ga oshdi. Yangi narx: ${self.narx}")
        elif tanlov == 2:
            yangi_narx = son_kirit("Yangi narxni kiriting ($): ")
            if yangi_narx > 0:
                self.narx = yangi_narx
                print(f"✅ Narx o'zgardi! Yangi narx: ${self.narx}")
            else:
                print("⚠️ Narx noldan baland bo'lishi kerak!")
        input("\n[Enter] bosing...")

# ================= 5-MASALA: EMPLOYEE =================
class Employee:
    def __init__(self, ism: str, fam: str, sana: str, lavozim: str, maosh: int):
        self.ism = ism
        self.fam = fam
        self.sana = sana
        self.lavozim = lavozim
        self.maosh = maosh
        self.bonus = 0

    def set_bonus(self):
        tozalash()
        print("🎁 BONUS HISOBLASH TIZIMI 🎁")
        print(f"Xodim: {self.ism} {self.fam} | Maoshi: {self.maosh:,} so'm")
        
        if self.maosh < 10000000:
            self.bonus = int(self.maosh * 0.25)
            jami = self.maosh + self.bonus
            print(f"🎉 Maosh 10 mln dan kam! 25% bonus berildi.")
            print(f"💵 Bonus miqdori: {self.bonus:,} so'm")
            print(f"💰 Jami qo'lga tegadigan summa: {jami:,} so'm")
        else:
            self.bonus = 0
            print("ℹ️ Maosh 10 mln so'mdan kam emas. Bonus berilmadi.")
        input("\n[Enter] bosing...")


# ================= BOSH MENU (TAKSIMLOVCHI) =================
def main():
    tozalash()
    print("✨ MUKAMMAL CLASS TIZIMIGA XUSH KELIBSIZ ✨")
    print("Qaysi masala tizimini ishga tushirmoqchisiz?")
    print("2. Restoran boshqaruvi")
    print("3. Ijtimoiy tarmoq (User)")
    print("4. Telefon do'koni")
    print("5. Xodimlar va Bonus tizimi")
    print("0. Dasturdan chiqish")
    
    m_tanlov = son_kirit("Tanlang >>> ")
    
    if m_tanlov == 0:
        print("Dastur tugatildi. Rahmat!")
        exit()
        
    elif m_tanlov == 2:
        res = Restoran("09:00 - 23:00", ["Palov", "Shashlik", "Somsa"])
        while True:
            tozalash()
            print(f"🍴 RESTORAN: Menyuda {len(res.menyu)} ta taom bor.")
            print("1. Ish vaqtini ko'rish")
            print("2. Menyuga ovqat qo'shish")
            print("0. Bosh menyuga qaytish")
            s = son_kirit("Amalni tanlang >>> ")
            if s == 0: break
            elif s == 1: res.get_work_time()
            elif s == 2: res.add_food()

    elif m_tanlov == 3:
        usr = User("Asilbek", "asil_coder")
        while True:
            tozalash()
            print(f"👤 USER: {usr.name} | Obunachilar: {len(usr.followers)} | Obunalari: {len(usr.following)}")
            print("1. Kimdir obuna bo'lish (Follow)")
            print("2. Obunani o'chirish (Unfollow)")
            print("3. Obunachini haydash (Remove Follower)")
            print("0. Bosh menyuga qaytish")
            s = son_kirit("Amalni tanlang >>> ")
            if s == 0: break
            elif s == 1: usr.follow()
            elif s == 2: usr.unfollow()
            elif s == 3: usr.remove_follower()

    elif m_tanlov == 4:
        ph = Phone("iPhone", "15 Pro", 1200, 2023)
        while True:
            tozalash()
            print(f"📱 TELEFON: {ph.brand} {ph.model} | Yili: {ph.yili} | Narxi: ${ph.narx}")
            print("1. Narxni o'zgartirish")
            print("0. Bosh menyuga qaytish")
            s = son_kirit("Amalni tanlang >>> ")
            if s == 0: break
            elif s == 1: ph.update_price()

    elif m_tanlov == 5:
        emp = Employee("Anvar", "Karimov", "2024-01-15", "Dasturchi", 8500000)
        while True:
            tozalash()
            print(f"👔 XODIM: {emp.ism} {emp.fam} | Lavozim: {emp.lavozim}")
            print("1. Bonusni hisoblash va berish")
            print("0. Bosh menyuga qaytish")
            s = son_kirit("Amalni tanlang >>> ")
            if s == 0: break
            elif s == 1: emp.set_bonus()

    # Dasturni davom ettirish so'rovi
    while True:
        yana = input("\nBoshqa masala tizimiga o'tishni xohlaysizmi? (ha/yoq): ").lower().strip()
        if yana == "ha":
            main()
            break
        elif yana == "yoq":
            print("Dastur butunlay tugatildi.")
            exit()
        else:
            print("⚠️ Faqat 'ha' yoki 'yoq' deb yozing!")

if __name__ == "__main__":
    main()
