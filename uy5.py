from translate import Translator

tarjimon = Translator(from_lang="uz", to_lang="en")
lugat = ["salom", "dastur", 2.5, "yordam", 34, "kitob"]
natija = {}

for sozi in lugat:
    if type(sozi) == str:
        tarjima = tarjimon.translate(sozi)
        natija[sozi] = tarjima.lower()

print(natija)
