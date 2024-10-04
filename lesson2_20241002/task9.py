# user: Polina Kuklina
# date creation: 03.10.2024

# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().

cof_a = float(input("Введите коэффициент А линейного уравнения A·x + B = 0: "))
cof_b = float(input("Введите коэффициент B линейного уравнения A·x + B = 0: "))

def linear_equation(cof_a, cof_b):
    return (0 - cof_b) / cof_a

print(f"Решение уравнение {cof_a} · x + {cof_b} = 0:\nx = {linear_equation(cof_a, cof_b)}")