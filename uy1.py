a = int(input("a = "))
b = int(input("b = "))
sonlar = [i for i in range(a, b) if i % 2 == 0]
print(f"sonlar={sonlar}")
