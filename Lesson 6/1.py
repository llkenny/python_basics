# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
from itertools import cycle

class TrafficLight:
    __color = ""
    __colors = {"Red": 7, "Yellow": 2, "Green": 3}

    def running(self):
        for self.__color in cycle(self.__colors):
            for _ in range(self.__colors[self.__color]):
                sleep(1)
                yield self.__color


trafficLight = TrafficLight()
for color in trafficLight.running():
    print(color)
