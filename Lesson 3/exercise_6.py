# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    def uppercase(char):
        return chr(ord(char) - 32)

    if len(word) > 1:
        return f'{uppercase(word[0])}{word[1:]}'
    else:
        return uppercase(word)


def uppercase(string):
    words = string.split(" ")
    uppercased = map(int_func, words)
    return " ".join(uppercased)

print(uppercase(input("Enter string: ")))
