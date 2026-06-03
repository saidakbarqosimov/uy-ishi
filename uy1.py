users = [
    'Abdulla Abdullaev', 
    'Samandar Asadov', 
    'Shaxnoza Jurayeva', 
    'Ikrom Karimov',
    'Gulnora Xalilova',
    'Ziyoda Yuldashova'
]

men = []
women = []

for user in users:
    if user.endswith('ov') or user.endswith('ev'):
        men.append(user)
    elif user.endswith('va'):
        women.append(user)

print("men =", men)
print("women =", women)
