with open("input.txt", "r") as file:
    ascii_numbers = file.read().split()

text_result = "".join([chr(int(num)) for num in ascii_numbers])

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text_result)
