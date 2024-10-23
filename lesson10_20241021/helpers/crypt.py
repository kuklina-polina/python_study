from .io import logger

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

if __name__ == "__main__":
    logger("ERROR", 1, 1, "Запущен файл с функцией самостоятельно")