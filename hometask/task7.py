# user: Polina Kuklina
# date creation: 03.10.2024

#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

a = float(input("Введите точку А на числовой оси: "))
b = float(input("Введите точку B на числовой оси: "))
c = float(input("Введите точку C на числовой оси: "))

def segment_len(num_1, num_2):
    return abs(num_1) + abs(num_2)
ac = segment_len(a, c)
bc = segment_len(b, c)

print(f"Длина отрезка АС = {ac}")
print(f"Длина отрезка BС = {bc}")
print(f"Сумма длин = {ac + bc}")