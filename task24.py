# user: Polina Kuklina
# date creation: 22.10.2024

#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

test2 = "8 5 12 12 15 , 0 23 15 18 12 4 !"
test = "8 5 12 12 15"
# test_input = input("Введите фразу в виде чисел с пробелами и знаками препинания: ")

def get_alphabet():
    alphabet = { str(i - (ord("a")-1)): chr(i) for i in range(ord("a"), ord("z") + 1) }
    alphabet ["0"] = " "
    return alphabet

def replace_num_to_letter(str_input):
    list_symbol = str_input.split(" ")
    list_letter_symbol = [get_alphabet()[key] if key in get_alphabet().keys() else key for key in list_symbol]
    print("".join(list_letter_symbol))

replace_num_to_letter(test)
replace_num_to_letter(test2)
# replace_num_to_letter(test_input)