# user: Polina Kuklina
# date creation: 08.10.2024

#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

input_array = range(0,100,10)
# input_array = list(input("Введите последовательность элементов массива через запятую: ").split(","))
# Можно взять для примера - 1,5,6,84,16,6146,133,2,0

def increase_array_by_one(array):
    new_array = []
    for value in array:
        new_array.append(int(value) + 1)
    return new_array

print(increase_array_by_one(input_array))