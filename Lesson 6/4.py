# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Car is running")

    def stop(self):
        print("Car stopped")

    def turn(self, direction):
        print(f"Changing direction: {direction}")

    def show_speed(self):
        return self.speed


class TownCar(Car):
    
    def show_speed(self):
        if self.speed > 60:
            print("Speed limit warning")
        return super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    
    def show_speed(self):
        if self.speed > 40:
            print("Speed limit warning")
        return super().show_speed()


class PoliceCar(Car):

    def __init__(self, speed):
        super().__init__(speed, "blue", "Police", True)
        pass


import io
import unittest
import unittest.mock
from functools import partial

class TestCarsParameters(unittest.TestCase):

    def parameters_test(self, type, speed, color, name, is_police):
        obj = type(speed, color, name, is_police)
        self.assertEqual(speed, obj.speed)
        self.assertEqual(color, obj.color)
        self.assertEqual(name, obj.name)
        self.assertEqual(is_police, obj.is_police)

    def test_car_parameters(self):
        self.parameters_test(Car, 20, "yellow", "Test", False)

    def test_sport_car_parameters(self):
        self.parameters_test(SportCar, 120, "red", "Test2", False)

    def test_work_car_parameters(self):
        self.parameters_test(SportCar, 55, "white", "Test3", False)


class TestCarsMethods(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def method_test(self, obj_class, method, output, mock_stdout):
        obj = obj_class(0, "", "", False)
        method(obj)
        self.assertEqual(mock_stdout.getvalue(), output)
        
    def test_go(self):
        for obj_class in [Car, TownCar, SportCar, WorkCar]:
            self.method_test(obj_class, obj_class.go, "Car is running\n")

    def test_stop(self):
        for obj_class in [Car, TownCar, SportCar, WorkCar]:
            self.method_test(obj_class, obj_class.stop, "Car stopped\n")

    def test_turn(self):
        for obj_class in [Car, TownCar, SportCar, WorkCar]:
            method = partial(obj_class.turn, direction = "right")
            self.method_test(obj_class, method, "Changing direction: right\n")

    def test_speed(self):
        for obj_class in [Car, TownCar, SportCar, WorkCar]:
            obj = obj_class(30, "", "", True)
            self.assertEqual(30, obj.show_speed())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def speed_limit_test(self, obj_class, speed, is_warning_expected, mock_stdout):
        obj = obj_class(speed, "", "", False)
        obj.show_speed()
        output = mock_stdout.getvalue()
        self.assertEqual(is_warning_expected, output == "Speed limit warning\n")

    def test_speed_limit(self):
        self.speed_limit_test(TownCar, 60, False)
        self.speed_limit_test(TownCar, 61, True)
        self.speed_limit_test(WorkCar, 40, False)
        self.speed_limit_test(WorkCar, 41, True)


class TestPoliceCarMethods(unittest.TestCase):

    def test_police_car_parameters(self):
        obj = PoliceCar(45)
        self.assertEqual(45, obj.speed)
        self.assertEqual(("blue", "Police", True), (obj.color, obj.name, obj.is_police))

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_go_police(self, mock_stdout):
        obj = PoliceCar(0)
        obj.go()
        self.assertEqual(mock_stdout.getvalue(), "Car is running\n")
            

if __name__ == '__main__':
    unittest.main()
