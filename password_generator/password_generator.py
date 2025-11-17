import random
import string

# Проверка на длину пароля
while True:
    length = int(input("Введите длину пароля (не меньше 6 символов): "))
    if length >= 6:
        break
    else:
        print("Слишком короткий пароль! Попробуйте снова.")

# Вывод меню выбора сложности пароля
print("Выберите сложность пароля:")
print("1 - Легкий (только буквы)")
print("2 - Средний (буквы + цифры)")
print("3 - Сложный (буквы + цифры + символы)")

# Выбор сложности пароля
while True:
    choice = input("Введите 1, 2 или 3: ")
    if choice in ["1", "2", "3"]:
        break
    else:
        print("Некорректный ввод, пропробуйте снова.")

# Реализация выдачи пароля по сложности
if choice == "1":
    chars = string.ascii_letters
elif choice == "2":
    chars = string.ascii_letters + string.digits
elif choice == "3":
    chars = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(chars) for _ in range(length))

print("Ваш пароль:", password)

with open("passwords.txt", "a") as f:
    f.write(password + "\n")