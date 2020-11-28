# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.

# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
#   проверить на практике работу декоратора @property.

from __future__ import annotations # Для использования типа в методе этого типа
from abc import ABC, abstractproperty

class Cloth(ABC):

    @abstractproperty
    def fabricAmount(self):
        pass

    @staticmethod
    def fabricTotal(clothes: [Cloth]):
        return sum([cloth.fabricAmount for cloth in clothes])



class Coat(Cloth):
    def __init__(self, size):
        self.size = size

    @property
    def fabricAmount(self):
        return self.size / 6.5 + 0.5


class Suit(Cloth):
    def __init__(self, height):
        self.height = height

    @property
    def fabricAmount(self):
        return 2 * self.height + 0.3


c = Coat(6.5)
s = Suit(10)
print(c.fabricAmount)
print(s.fabricAmount)

total = Cloth.fabricTotal([s, c])
print(total)
