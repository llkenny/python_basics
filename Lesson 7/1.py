# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.

# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

# Примеры матриц вы найдете в методичке.

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

# Далее реализовать перегрузку метода __add__() для реализации операции сложения 
#   двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой 
#   строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

from functools import reduce

class Matrix:
    
    def __init__(self, data: [[]]):
        self.data = data

    def __str__(self):
        try:
            rows = map(lambda row: reduce(lambda x, y: f'{x} {y}', row), self.data)
            return reduce(lambda x, y: f'{x}\n{y}', rows)
        except:
            raise Exception(f'Matrix is empty or invalid')

    def __add__(self, other):
        if type(other) == Matrix:
            return Matrix(list(map(lambda r_pair: list(map(sum, zip(r_pair[0], r_pair[1]))), zip(self.data, other.data))))
        raise ValueError('Unsupported type')


m1 = Matrix([[1, 1], [2, 2], [3, 3]])
m2 = Matrix([[0.1, 0.1], [0.2, 0.2], [0.3, 0.3]])
m3 = Matrix([[0.01, 0.01], [0.02, 0.02], [0.03, 0.03]])

print(f'{m1}\n+\n{m2}\n+\n{m3}\n=\n{m1 + m2 + m3}')
