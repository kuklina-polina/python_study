# user: Polina Kuklina
# date creation: 03.10.2024

# todo: Проверить истинность высказывания:
#  "Данное четырехзначное число читается одинаково слева направо и справа налево".

number = int(input("Введите четырехзначное число: "))
if not (999 < number <= 9999):
    exit("Число не четырехзначное!")

if str(number) == str(number)[::-1]:
    print("Данное четырехзначное число читается одинаково слева направо и справа налево")
else:
    print("Число не является палиндромом")