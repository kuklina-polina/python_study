# user: Polina Kuklina
# date creation: 17.10.2024

# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.
# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

def crypting_line(line, sdvig):
    # массивы кодов ASCII генератором списков
    up = [code for code in range(ord("А"), ord("Я")+1)]
    low = [code for code in range(ord("а"), ord("я")+1)]
    line_new = ""
    for symbol in line:
        if ord(symbol) in up:
            line_new += chr(up[(up.index(ord(symbol)) - sdvig) % 32])
        elif ord(symbol) in low:
            line_new += chr(low[(low.index(ord(symbol)) - sdvig) % 32])
        else:
            line_new += symbol
    return line_new

def crypting_text_from_file(file):
    cryp_text = ""
    f = open(file, "rt", encoding="utf-8")
    lines = f.readlines()
    f.close()
    for line in lines:
        cryp_text += crypting_line(line, lines.index(line)+1)
    return cryp_text

ciphertext = crypting_text_from_file("message.txt")
print(ciphertext)

