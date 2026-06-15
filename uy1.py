class Talaba:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Kurs:
    def __init__(self, kurs_name, kurs_teacher):
        self.kurs_name = kurs_name
        self.kurs_teacher = kurs_teacher
        self.talabalar_soni = 0
        self.talabalar = []

    def add(self, new_student):
        self.talabalar.append(new_student)
        self.talabalar_soni += 1

    def delete(self, student):
        if student in self.talabalar:
            self.talabalar.remove(student)
            self.talabalar_soni -= 1

    def info_kurs(self):
        print(f"Kurs: {self.kurs_name} | O'qituvchi: {self.kurs_teacher} | Talabalar soni: {self.talabalar_soni}")
        for t in self.talabalar:
            print(f"- {t.name}, {t.age} yosh")

# 2 ta kurs yaratish
kurs1 = Kurs("Python Backend", "Anvar Narzullayev")
kurs2 = Kurs("Frontend React", "Sardor Ahmedov")

# 10 tadan talaba yaratish va qo'shish
for i in range(1, 11):
    s1 = Talaba(f"Talaba_{i}", 18 + i % 5)
    s2 = Talaba(f"Student_{i}", 19 + i % 4)
    kurs1.add(s1)
    kurs2.add(s2)

# O'chirish uchun talabalarni saqlab qo'yamiz va haydaymiz
haydaladigan1 = kurs1.talabalar[0]
haydaladigan2 = kurs1.talabalar[1]

kurs1.delete(haydaladigan1)
kurs1.delete(haydaladigan2)

# Natijani tekshirish
kurs1.info_kurs()
