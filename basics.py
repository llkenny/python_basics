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

# 3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
s = input("Enter number (int): ")
sum = int(s)
j = 3
while j > 1:
    sum += int(s * j)
    j -= 1
print(f"Sum: {sum}")

# 4
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
i = int(input("Enter number (int): "))
max = i % 10
i //= 10
while i > 0:
    check = i % 10
    i //= 10
    if check > max:
        max = check
    if max == 9:
        break
print(f"Max digit is {max}")