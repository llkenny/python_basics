# 1
i = 0
b = True
f = 0.2
s = "string"

print(f"{i} {b} {f} {s}")

i = int(input("Enter new integer value: "))
s = input("Enter new string: ")
print(f"{i} {b} {f} {s}")

# 2
# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
t = int(input("Enter time in seconds: "))
h = t // 3600 % 24
m = t // 60 % 60
s = t % 60
print(f"{h:02}:{m:02}:{s:02}")