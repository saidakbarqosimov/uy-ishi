class String:
    def to_lower(self, matn):
        result = ""
        for char in matn:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char
        return result

    def to_upper(self, matn):
        result = ""
        for char in matn:
            if 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            else:
                result += char
        return result

    def is_lower(self, matn):
        has_alpha = False
        for char in matn:
            if 'A' <= char <= 'Z':
                return False
            if 'a' <= char <= 'z':
                has_alpha = True
        return has_alpha

    def is_upper(self, matn):
        has_alpha = False
        for char in matn:
            if 'a' <= char <= 'z':
                return False
            if 'A' <= char <= 'Z':
                has_alpha = True
        return has_alpha

# Tekshirish
st = String()
print(st.to_lower("Dasturchi LPT"))  # dasturchi lpt
print(st.is_upper("HELLO"))          # True
