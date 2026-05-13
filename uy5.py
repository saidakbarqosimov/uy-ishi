car_count = {
    "Chevrolet": 120,
    "Toyota": 95,
    "BMW": 60,
    "Kia": 75
}

eng_kop_sotilgan = max(car_count, key=car_count.get)
eng_kam_sotilgan = min(car_count, key=car_count.get)

print("Eng ko'p sotilgan mashina:", eng_kop_sotilgan, "-", car_count[eng_kop_sotilgan], "ta")
print("Eng kam sotilgan mashina:", eng_kam_sotilgan, "-", car_count[eng_kam_sotilgan], "ta")

