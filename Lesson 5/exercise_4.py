"""Создать (не программно) текстовый файл со следующим содержимым:

One — 1

Two — 2

Three — 3

Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

tr = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('numbers.txt', 'r') as f_in, open('numbers_out.txt', 'w') as f_out:
    for line_in in f_in:
        split = line_in.split(" — ")
        if split[0] in tr.keys():
            split[0] = tr[split[0]]
            line_out = " — ".join(split)
        else:
            line_out = line_in
        f_out.write(line_out)
