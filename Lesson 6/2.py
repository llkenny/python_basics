# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.

# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    _length: float
    _width: float

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def total_mass(self, mass, thickness):
        return self._length * self._width * mass * thickness


road = Road(5000, 20)
print(f'{road.total_mass(25, 5) / 1000} т')
