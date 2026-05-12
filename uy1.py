set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

umumiy = set1.intersection(set2)
faqat_birinchi = set1.difference(set2)

natija = sum(umumiy) - sum(faqat_birinchi)
print(natija) 
