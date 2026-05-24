with open("sonlar.txt", "r") as file:
    numbers = [int(x) for x in file.read().split()]

ortacha_qiymat = round(sum(numbers) / len(numbers))
print(ortacha_qiymat)
