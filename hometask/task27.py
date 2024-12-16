# user: Polina Kuklina
# date creation: 23.10.2024

#todo:
# 1. Создайте виртуальное окружение через терминал в текущей папки нового проекта.
# Название окружению дайте по названию проекта. Переключитесь на созданное новое окружение.
# 2. Установите пакет pandas.
# Убедитесь что он установился и добавился в папку виртуального окружения.
# 3. Создайте файл test_package.py в него добавьте строки
# import pandas as pd
# pd.test()
# Убедитесь что пакет подкючен.
# 4. Создайте свой пакет helpers со структурой
# helpers
#     __init__.py
#     io.py
#     crypt.py
# В модуль io.py разместите ранее написаный logger
# В модуль crypt.py добавьте функцию шифра цезаря.
# 5. Содайте новый файл main.py  Подключите в него функцию логера и шифрования.
# Проверьте их работу.

from helpers import logger, crypting_text_from_file

files_for_crypt = ["message.txt", False]

for file in files_for_crypt:
    if file == False:
        logger("ERROR", 1, 1, "Файла для шифрования нет")
    else:
        print(crypting_text_from_file(file))

