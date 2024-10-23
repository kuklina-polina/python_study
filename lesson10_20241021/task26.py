# user: Polina Kuklina
# date creation: 23.10.2024

#todo Задача 1. Чтение матрицы, load_matrix(filename)
# Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)
# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36
# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.
# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!

def load_matrix(filename):
    file = open(filename, "rt", encoding= "utf-8")
    lines_list = [list(map( lambda x: int(x), line.strip("\n").split(" "))) for line in file.readlines()]
    if len({len(list) for list in lines_list}) == 1:
        return lines_list
    else:
        return False

print(load_matrix("file_for_task26.txt"))