# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def div(x, y):
    if y == 0:
        raise Exception("Division by zero")
    return x / y

x = float(input("Enter x: "))
y = float(input("Enter y: "))

print(div(x, y))
