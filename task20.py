# user: Polina Kuklina
# date creation: 15.10.2024

#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

# Создание файла с текстом
f = open("import_this.txt", "wt", encoding="utf-8")
text_ = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
f.write(text_)
f.close()

def invert_text_file(name_file):
    f = open(name_file, "rt", encoding="utf-8")
    text_lines = f.readlines()
    for i in text_lines[::-1]:
        print(i[:-1])
    f.close()

invert_text_file("import_this.txt")
