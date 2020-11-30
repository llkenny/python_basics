# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

def lines_words(filename):
    lines = 0
    words = list()
    with open(filename, 'r') as file:
        for line in file:
            lines += 1
            words.append(len(line.split(' ')))
    return lines, words


l_w = lines_words('randomtext.txt')
print(f'Total lines: {l_w[0]}, words in lines: {l_w[1]}')
