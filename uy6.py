filmlar = {
    "Titanic": "Jack Dawson",
    "Harry Potter": "Harry Potter",
    "The Dark Knight": "Bruce Wayne (Batman)",
    "The Matrix": "Neo (Thomas Anderson)",
    "Forrest Gump": "Forrest Gump",
    "Gladiator": "Maximus Decimus Meridius",
    "Inception": "Dom Cobb",
    "Spider-Man": "Peter Parker",
    "Iron Man": "Tony Stark",
    "The Lord of the Rings": "Frodo Baggins"
}

film = input("Film nomini kiriting: ")

try:
    print(filmlar[film])
except KeyError:
    print("Bunday film yo'q")
