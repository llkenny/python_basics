# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. 
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. 
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

from abc import ABC, abstractmethod

units = ['WH', 'BK', 'AD', 'MD']

class WarehouseError(Exception):
    """Ошибки склада
    """
    def __init__(self, *args):
        self.text = args[0]


class OfficeEquipment(ABC):
    """Базовый класс для техники
    """
    def __init__(self, title):
        self.title = title
        self.unit = units[0]

    @abstractmethod
    def self_test(self):
        """Провести тестовый запуск устройства
        """
        pass


class Warehouse():
    """Класс склада
    """
    __items = list()

    def __init__(self, size):
        if type(size) is not int:
            raise WarehouseError('Size must be int')
        self.size = size

    def __str__(self):
        return str(self.report())

    def buy(self, item_type, vendor, count):
        """Закупить технику

        Args:
            item_type: Тип требуемой техники
            vendor: Производитель
            count: Количество
            
        Raises:
            WarehouseError: Ошибка склада
        """
        if type(count) is not int:
            raise WarehouseError('Count must be int')
        if type(vendor) is not str:
            raise WarehouseError('Vendor must be string')
        if not issubclass(item_type, OfficeEquipment):
            raise WarehouseError('Unknown office equipement')

        for _ in range(count):
            self.put(item_type(vendor))

    def put(self, item: OfficeEquipment):
        """Добавить технику на склад

        Args:
            item (OfficeEquipment): Добавляемая техника

        Raises:
            WarehouseError: Ошибка склада
        """
        if self.size - len(self.__items) <= 0:
            raise WarehouseError('Warehouse is full')
        if not issubclass(type(item), OfficeEquipment):
            raise WarehouseError('Unknown office equipement')
        item.unit = units[0]
        self.__items.append(item)

    def pop(self, item_type, unit):
        """Взять технику со склада

        Args:
            item_type: Тип требуемой техники
            unit: Подразделене - получатель

        Raises:
            WarehouseError: Ошибка склада

        Returns:
            [OfficeEquipment]: Единица техники
        """
        if unit not in units:
            raise WarehouseError('Wrong unit: ', unit)
        if not issubclass(item_type, OfficeEquipment):
            raise WarehouseError('Unknown office equipement')
        for item in self.__items:
            if type(item) is item_type:
                self.__items.remove(item)
                item.unit = unit
                return item
        raise WarehouseError('No item found: ', item_type)

    def report(self):
        """Выдать отчет об имеющейся технике

        Returns:
            [dict]: Словарь с ключами 'Title' и 'Unit'
        """
        r = list()
        for item in self.__items:
            r.append({'Title': item.title, 'Unit': item.unit})
        return r

    def clean(self):
        """Очистить склад
        """
        for item in self.__items:
            item.unit = None
        self.__items.clear()


class PrinterError(Exception):
    def __init__(self, *args):
        self.text = args[0]


class Printer(OfficeEquipment):
    """Класс 'Принтер'
    """
    def __init__(self, title, cartridge_capacity=None):
        if cartridge_capacity is None:
            self.cartridge_capacity = 0
        elif type(cartridge_capacity) is not int:
            raise PrinterError('Cartridge capacity must be int')
        self.cartridge_capacity = cartridge_capacity
        super().__init__(title)

    def self_test(self):
        self.print(['Test page printing'])

    def print(self, sheets: [str]):
        """Печать

        Args:
            sheets ([str]): Список текста (в страницах) для печати

        Raises:
            PrinterError: Ошибка принтера
        """
        for s in sheets:
            if self.cartridge_capacity <= 0:
                raise PrinterError('Replace cartridge')
            print(f'Printing: {s}')
            self.cartridge_capacity -= 1

    def reload(self, cartridge_capacity):
        """Замена картриджа

        Args:
            cartridge_capacity: Емкость нового картриджа

        Raises:
            PrinterError: Ошибка принтера
        """
        if type(cartridge_capacity) is not int:
            raise PrinterError('Cartridge capacity must be int')
        self.cartridge_capacity = cartridge_capacity


class ScannerError(Exception):
    def __init__(self, *args):
        self.text = args[0]


class Scanner(OfficeEquipment):
    """Класс 'Сканер'
    """
    def scan(self, sheets, receiver):
        """Отсканировать листы

        Args:
            sheets: Список листов
            receiver: Получатель скана

        Raises:
            ScannerError: Ошибка сканера
        """
        for s in sheets:
            if type(s) is not str:
                raise ScannerError('Unable to scan page', s)
            print("Scanning...")
            receiver(s)

    def self_test(self):
        self.scan(['Test page scanning'], print)


class Copier(Printer, Scanner):
    """Класс 'Копир'
    """
    def copy(self, sheets):
        """Сделать копии листов

        Args:
            sheets: Список листов
        """
        memory = list()
        def cache(s):
            memory.append(s)
        for s in sheets:
            super().scan([s], cache)
        super().print(memory)

    def self_test(self):
        self.copy(['Test page scanning'])


wh = Warehouse(10)

p = Printer('HP', 100)
p.print(['List 1'])
p.self_test()
assert p.cartridge_capacity == 98

try:
    wh.pop(Printer, units[3])
except Exception as err:
    print(type(err), err)

wh.put(p)
print(wh.report())
p = wh.pop(Printer, units[1])
assert p.unit == units[1]
print(wh.report())
p.print(['List 2'])
assert p.cartridge_capacity == 97

wh.put(p)
wh.clean()
print(wh.report())

s = Scanner('Epson')
s.scan(['Test'], print)

c = Copier('Xerox', 2)
c.copy(['Test copy 1', 'Test copy 2'])

wh.buy(Printer, "Canon", 8)
print(wh)
