def is_anagram(soz1, soz2):
    return sorted(soz1.lower()) == sorted(soz2.lower())

print(is_anagram("listen", "silent")) 
print(is_anagram("apple", "angel"))  
print(is_anagram("thing", "night"))  
