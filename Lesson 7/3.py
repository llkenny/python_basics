# Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
#   сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# 
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
#   умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.

# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.

# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

from functools import reduce

class Cell():
    def __init__(self, cells_number: int):
        self.cells_number = cells_number

    def __add__(self, other):
        if type(other) == Cell:
            return Cell(self.cells_number + other.cells_number)
        raise ValueError('Unsupported type')

    def __sub__(self, other):
        if type(other) == Cell:
            r = self.cells_number - other.cells_number
            if r > 0:
                return Cell(r)
            raise Exception('Sub result is less than zero')
        raise ValueError('Unsupported type')

    def __mul__(self, other):
        if type(other) == Cell:
            return Cell(self.cells_number * other.cells_number)
        raise ValueError('Unsupported type')

    def __truediv__(self, other):
        if type(other) == Cell:
            try:
                return Cell(self.cells_number / other.cells_number)
            except ZeroDivisionError:
                raise Exception('Other cell is empty')
        raise ValueError('Unsupported type')

    def make_order(self, cells_in_row):
        try:
            dm = divmod(self.cells_number, cells_in_row)
            result = ""
            if dm[0] > 0:
                result += f'{"*" * cells_in_row}'
                if dm[0] > 1:
                    result += f'\n{"*" * cells_in_row}' * (dm[0] - 1) # Для исключения конечного \n
            if dm[1] > 0:
                result += f'\n{"*" * dm[1]}'
            return result
        except ZeroDivisionError:
                raise Exception('Invalid data')
