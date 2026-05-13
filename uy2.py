movies = {
    "Titanic": 1997,
    "Avatar": 2009,
    "Inception": 2010,
    "Interstellar": 2014
}

print("2000-yildan keyingi filmlar:")

for nom, yil in movies.items():
    if yil > 2000:  
        print(nom) 
