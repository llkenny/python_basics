# Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
#   name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


import unittest

class TestPosition(unittest.TestCase):

    def position_test(self, name, surname, position, wage, bonus, fullname, income):
        obj = Position(name, surname, position, wage, bonus)
        self.assertEqual(name, obj.name)
        self.assertEqual(surname, obj.surname)
        self.assertEqual(position, obj.position)

        self.assertEqual(fullname, obj.get_full_name())
        self.assertEqual(income, obj.get_total_income())
        
    def test_first(self):
        self.position_test("", "", "", 0, 0, " ", 0)

    def test_second(self):
        self.position_test("Ivan", "Ivanovich", "CEO", 100, 5, "Ivan Ivanovich", 105)

if __name__ == '__main__':
    unittest.main()
