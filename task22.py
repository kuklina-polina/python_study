# user: Polina Kuklina
# date creation: 17.10.2024

#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.
#Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11

def read_text(file):
    f = open(file, "rt", encoding="utf-8")
    text_ = f.read()
    f.close()
    return text_


def count_vowels_in_text(str_text, local):
    vowels = {"ru": "аеёиоуыэюя", "en": "aeiou"}
    for letter in vowels[local]:
        if letter in str_text:
            print(f"Количество букв {letter} – {str_text.count(letter)}")

count_vowels_in_text(read_text("dump.txt"), "ru")
count_vowels_in_text(read_text("dump.txt"), "en")