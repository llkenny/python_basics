# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

filename = 'numbers_line.txt'

def write(numbers):
    with open(filename, 'w') as file:
        file.write(" ".join(numbers))


def file_sum():
    with open(filename, 'r') as file:
        numbers = file.readline().split(" ")
        return sum(map(float, numbers))


def exercise():
    numbers = list()

    while True:
        s = input("Enter new number or press enter: ")
        if len(s) == 0:
            break
        else:
            numbers.append(s)

    write(numbers)
    return file_sum()


print(exercise())

