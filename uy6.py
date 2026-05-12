set1 = {4, 5, 6, 7, 8, 9}
set2 = {5, 6, 7, 10, 11}

umumiy_emas = set1 ^ set2 
umumiy = set1 & set2      

natija = sum(umumiy_emas) - sum(umumiy)
print(natija) # Output: 24 (42 - 18)
