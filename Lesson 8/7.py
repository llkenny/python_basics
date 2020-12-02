# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b > 0:
            if self.b == 1:
                return f'{self.a} + i'
            return f'{self.a} + {self.b}i'
        elif self.b < 0:
            if self.b == -1:
                return f'{self.a} - i'
            return f'{self.a} - {self.b * -1}i'
        else:
            return f'{self.a}'

    def __add__(self, other):
        if type(other) is not ComplexNumber:
            raise ValueError('Operation undefined')
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        if type(other) is not ComplexNumber:
            raise ValueError('Operation undefined')
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + self.b * other.a
        return ComplexNumber(a, b)



assert str(ComplexNumber(1, 2)) == '1 + 2i'
assert str(ComplexNumber(-1, -2)) == '-1 - 2i'
assert str(ComplexNumber(1, 0)) == '1'

assert str(ComplexNumber(2, 2) + ComplexNumber(-1, -3)) == '1 - i'
assert str(ComplexNumber(2, 2) * ComplexNumber(-1, -3)) == '4 - 8i'
