set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

farq = set1 ^ set2
natija = sorted(farq, reverse=True)
print(*natija) # Output: 9 8 7 3 2 1
