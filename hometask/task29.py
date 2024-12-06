# user: Polina Kuklina
# date creation: 30.11.2024

#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной
# функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции,
# кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

from datetime import datetime

def decorator_counter(fn):
    fn_name = fn.__name__
    count = 0
    datetime_ = None

    def wrapper(*args, **kwargs):
        nonlocal count, datetime_
        count += 1
        datetime_ = datetime.now().strftime("%d.%m.%Y %H:%M")
        res = fn(*args, **kwargs)
        return res

    def save():
        with open("debug.log", "a") as f:
            f.write(f"{fn_name}, {count}, {datetime_}\n")

    wrapper.save_info = save
    return wrapper

@decorator_counter
def add(a, b):
    return a + b

@decorator_counter
def invert(a):
    return -a

# Вызовы функций
for i in range(0,25):
    invert(i)
add(2, 4)
invert(5)
invert(-7)
add(8, 4)

#Статистика записывается по всему файлу
add.save_info()
invert.save_info()