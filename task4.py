# user: Polina Kuklina
# date creation: 01.10.2024

# todo: Заданы три числа в переменных x, y, z.
# Напечатать наибольшее из этих чисел.
# Пример:
# x = 10
# y = 15
# z = 2
# Ответ:
# Наибольшее число 15

x = int(input("Введите x: \n"))
y = int(input("Введите y: \n"))
z = int(input("Введите z: \n"))
if x > y and x > z:
    print(f"Наибольшее число {x}")
elif y > x and y > z:
    print(f"Наибольшее число {y}")
else:
    print(f"Наибольшее число {z}")

# Пример:
# x = 77
# y = 9
# z = 130
# Ответ:
# Наибольшее число 130