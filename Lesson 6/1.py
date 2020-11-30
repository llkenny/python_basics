# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
from itertools import cycle

class Light:
    name: str
    time: float

    def __init__(self, name, time):
        self.name = name
        self.time = time

class TrafficLight:
    __color = ""
    __lights = [Light("Red", 7), Light("Yellow", 2), Light("Green", 5)]

    def running(self):
        for light in cycle(self.__lights):
            self.__color = light.name
            for _ in range(light.time):
                sleep(light.time)
                yield self.__color


for color in TrafficLight().running():
    print(color)
