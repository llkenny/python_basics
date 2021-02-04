# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

feb = 2
shorts = [4, 6, 9, 11]

m_exc = ValueError("Incorrect month")
d_exc = ValueError("Incorrect day")

class Date():
    def __init__(self, string):
        self.string = string

    def to_list(self):
        return list(map(int, self.string.split("-")))

    @staticmethod
    def format_check(string):
        d, m, y = tuple(Date(string).to_list())
        if m not in range(1, 13):
            raise m_exc
        if d <= 0:
            raise d_exc

        if m == feb: # feb check
            is_leap = not bool(y % 4)
            if (is_leap and d > 29) or (not is_leap and d > 28):
                raise d_exc
        elif (m in shorts and d > 30) or d > 31: # short or long months check
            raise d_exc


import pytest

def test_format():
    assert Date("22-11-2020").to_list() == [22, 11, 2020]

def test_success():
    assert Date.format_check("22-11-2020") is None
    assert Date.format_check("1-01-1300") is None
    assert Date.format_check("29-02-2020") is None
    assert Date.format_check("28-02-2021") is None
    assert Date.format_check("31-12-1300") is None
    
def test_failures():
    with pytest.raises(ValueError, match="Incorrect month"):
        Date.format_check("22-13-2020")
        Date.format_check("1-0-1300")
    with pytest.raises(ValueError, match="Incorrect day"):
        Date.format_check("29-02-2020")
        Date.format_check("30-02-2021")
        Date.format_check("31-3-1300")
