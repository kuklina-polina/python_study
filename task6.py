# user: Polina Kuklina
# date creation: 03.10.2024

#todo: Дана сторона квадрата a. Найти его площадь S = a²
# Примечание: сторону квадрата получаем через функцию input().

a = float(input("Введите сторону квадрата: "))

def area_square(side):
    return side**2

print(f"Площадь квадрата со стороной {a} = {area_square(a)}")
