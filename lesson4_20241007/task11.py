# user: Polina Kuklina
# date creation: 08.10.2024

# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

input_year = int(input("Введите год: "))

def century_by_year(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

century = century_by_year(input_year)

print(f"Год {input_year} относится к {century} столетию.")