# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivException(Exception):
    def __init__(self, *args, **kwargs):
        self.text = args[0]
        

def my_div(x, y):
    if not y:
        raise MyZeroDivException("Division by zero", {'x': x, 'y': y})
    return x / y


def test(*args):
    for arg in args:
        try:
            print(my_div(arg[0], arg[1]))
        except Exception as err:
            print(type(err), err)


test((1, 0), (1, 1))
