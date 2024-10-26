# user: Polina Kuklina
# date creation: 08.10.2024

# todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

input_array = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]
# input_array = list(input("Введите последовательность элементов массива через запятую: ").split(","))
# Можно взять для примера - 1,2,3,84,1,2,1,3,13

# Функция возвращает  значения с минимальной суммой в массиве (так как массив из индексов - то все целочисленные
# и положительные и упорядочены в порядке возрастания)
def two_values_min_sum(array):
    dist_array = []
    for key in range(0, len(array) - 1):
        dist_array.append((array[key + 1] - array[key]))
    index_min_dist = dist_array.index(min(dist_array))
    return [array[index_min_dist], array[index_min_dist + 1]]

# Словарь из уникальных значений массива и индексами положения значений, где ключи стали значениями, а значения - ключами))))))))
dict_value = {}
for key, value in enumerate(input_array):
    if value in dict_value:
        dict_value[value].append(key)
    else:
        dict_value[value] = [key]

# Итерация по словарю и проверка по условию "сколько раз встретилось значение", если больше одного то выполняется функция
for value in dict_value:
    if len(dict_value[value]) == 1:
        print(f"Для числа {value} нет минимального растояния, т.к элемент в массиве один.")
    else:
        key1, key2 = two_values_min_sum(dict_value[value])
        print(f"Для числа {value} минимальное растояние в массиве по индексам: {key1} и {key2}.")