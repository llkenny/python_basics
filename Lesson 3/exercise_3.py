# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(x, y, z):
    array = [x, y, z]
    return sum(array) - min(array)
    