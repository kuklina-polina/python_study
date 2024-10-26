# user: Polina Kuklina
# date creation: 22.10.2024

#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
def crypting_line(line, sdvig):
    # массивы кодов ASCII генератором списков
    up = [code for code in range(ord("A"), ord("Z")+1)]
    low = [code for code in range(ord("a"), ord("z")+1)]
    line_new = ""
    for symbol in line:
        if ord(symbol) in up:
            line_new += chr(up[(up.index(ord(symbol)) + sdvig) % 26])
        elif ord(symbol) in low:
            line_new += chr(low[(low.index(ord(symbol)) + sdvig) % 26])
        else:
            line_new += symbol
    return line_new

def many_variants(string_input):
    for i in range(26):
        a = crypting_line(string_input, i)
        print(f"{i}. {a}")

test = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

many_variants(test)
result = input("Введите номер читабельной строки: ")
print(f"Вероятнее всего данная строка была зашифрована шифром Цезаря со сдвигом {result}.")

