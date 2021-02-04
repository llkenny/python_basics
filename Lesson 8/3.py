# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class InputError(Exception):
    def __init__(self, *args):
        self.text = args[0]


result = list()

while True:
    s = input('Add number (type "stop" to exit): ')
    if s == "stop":
        break
    try:
        try: 
            result.append(int(s))
        except ValueError:
            raise InputError('Bad input data')
    except Exception as err:
        print(f'{type(err)}, {err}')
    else:
        print(f'{s} was added\nCurrent list: {result}')
    finally:
        print('\n')

