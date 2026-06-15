class Convertor:
    def __init__(self):
        # Transliteratsiya lug'ati
        self.en_to_ru_map = {
            'A': 'А', 'B': 'Б', 'V': 'В', 'G': 'Г', 'D': 'Д', 'E': 'Е', 'Yo': 'Ё', 'Zh': 'Ж',
            'Z': 'З', 'I': 'И', 'Y': 'Й', 'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О',
            'P': 'П', 'R': 'Р', 'S': 'С', 'T': 'Т', 'U': 'У', 'F': 'Ф', 'Kh': 'Х', 'Ts': 'Ц',
            'Ch': 'Ч', 'Sh': 'Ш', 'Shch': 'Щ', 'Yu': 'Ю', 'Ya': 'Я',
            'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д', 'e': 'е', 'yo': 'ё', 'zh': 'ж',
            'z': 'з', 'i': 'и', 'y': 'й', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о',
            'p': 'п', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'f': 'ф', 'kh': 'х', 'ts': 'ц',
            'ch': 'ч', 'sh': 'ш', 'shch': 'щ', 'yu': 'ю', 'ya': 'я'
        }
        # Teskari lug'at yaratish
        self.ru_to_en_map = {v: k for k, v in self.en_to_ru_map.items()}

    def en_to_ru(self, text):
        # Murakkab harflarni (Yo, Yu, Ya, Ch, Sh) birinchi almashtiramiz
        for key in ['Yo', 'Zh', 'Kh', 'Ts', 'Ch', 'Sh', 'Yu', 'Ya', 'yo', 'zh', 'kh', 'ts', 'ch', 'sh', 'yu', 'ya']:
            if key in self.en_to_ru_map:
                text = text.replace(key, self.en_to_ru_map[key])
        
        # Qolgan bitta harflilarni almashtiramiz
        result = ""
        for char in text:
            result += self.en_to_ru_map.get(char, char)
        return result

    def ru_to_en(self, text):
        result = ""
        for char in text:
            result += self.ru_to_en_map.get(char, char)
        return result

# Tekshirish
conv = Convertor()
print(conv.en_to_ru("Salom dunyo"))  # Салом дунё
