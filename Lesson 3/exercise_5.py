# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, 
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

stop = "exit"

def string_to_sum(start = 0):
    new_str = input(f"Enter new values, type {stop} for stop: ")
    values = new_str.split(" ")
    
    if stop in values:
        index = values.index("exit")
        return start + sum(list(map(int, values[:index])))
    else:
        new_sum = start + sum(list(map(int, values)))
        print(f'Current sum: {new_sum}')
        return string_to_sum(new_sum)

print(string_to_sum())
