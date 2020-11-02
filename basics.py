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

# 5
# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
proceeds = float(input("Enter proceeds (positive float): "))
outgo = float(input("Enter outgo (positive float): "))
if proceeds < 0 or outgo < 0:
    print("Bad input")
else:
    if proceeds == outgo:
        print("Result: zero")
    else:
        negative_msg = "Result: loss"
        if outgo > proceeds:
            print(negative_msg)
        else:
            profit = proceeds - outgo
            print(f"Result: profit = {profit}")
            print(f"Profitability of proceeds: {profit / proceeds}") # proceeds не может быть 0, т.к. outgo >= 0, proceeds != outgo, proceeds > outgo 
            count = int(input("Enter number of employees: "))
            if count != 0:
                print(f"Profit per employee: {profit / count}")
        
# 6
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
a = float(input("Enter first result (float): "))
b = float(input("Enter goal (float): "))
if a == 0:
    print(f"Running is not for you")
else:
    days = 1
    while a < b:
        a *= 1.1
        days += 1
    print(f"Days to goal: {days}")