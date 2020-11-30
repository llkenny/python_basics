# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = "канцелярская принадлежность"

    def draw(self):
        return "Запуск отрисовки."


class Pen(Stationery):
    title = "ручка"

    def draw(self):
        return f'{self.title}: {super().draw()}'


class Pencil(Stationery):
    title = "карандаш"

    def draw(self):
        return f'{self.title}: {super().draw()}'


class Handle(Stationery):
    title = "маркер"

    def draw(self):
        return f'{self.title}: {super().draw()}'


for obj_class in [Pen, Pencil, Handle]:
    print(obj_class().draw())
