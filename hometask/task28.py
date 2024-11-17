# user: Polina Kuklina
# date creation: 17.11.2024

#todo: Реализовать в игре "Поле чудес" возможность сохранять состояние игры (save game).
# Пользователю должна быть предоставлена возможность восстановиться из файла сериализации.
# Сохранить слово, кол-во истраченных баллов и отгаданные буквы.


from random import randint as ri
import pickle
import os


def save_game(word, attempt, field):
    obj = {"word": None,
           "attempt": None,
           "field": None}
    name_save_game = input("Сохранить как: ")
    obj["word"] = word
    obj["attempt"] = attempt
    obj["field"] = field
    with open(name_save_game + ".pkl", 'wb') as fp:
        pickle.dump(obj, fp)
    exit(0)

def init():
    global words, desc_
    words = ["оператор", "конструкция", "объект"]
    desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования.",
             "Это синтаксическая структура, которая определяет способ организации кода.",
             "Это сущность, представляющая собой экземпляр класса." ]

def get_word():
    global words, desc
    word_index = ri(0, len(words) - 1)
    print_(word_index)
    return words[word_index]

def print_(word_index):
    global desc_
    print("Угадайте слово по подсказке: " + desc_[word_index] + "\nУ Вас есть 10 штрафных баллов!")

def get_field(word_for_play):
    return [" ▒"] * len(word_for_play)

def get_attempt():
    global attempt
    return attempt

def set_attempt():
    global attempt
    attempt += 1

def get_letter():
    match get_attempt():
        case 1:
            letter = input(f"\nВы истратили {get_attempt()} штрафной балл! \nВведите букву: ")
        case 2 | 3 | 4:
            letter = input(f"\nВы истратили {get_attempt()} штрафных балла! \nВведите букву: ")
        case _:
            letter = input(f"\nВы истратили {get_attempt()} штрафных баллов! \nВведите букву: ")
    return letter

def engine(word_for_play, player_word):
    while 0 <= get_attempt() < 10 and " ▒" in player_word:
        letter = get_letter()
        if letter in word_for_play:
            start = 0
            for j in range(word_for_play.count(letter)):
                 indx = word_for_play.index(letter, start)
                 player_word[indx] = " " + letter
                 start = indx + 1
        elif letter == "2":
            save_game(word_for_play, get_attempt(), player_word)
        else:
            print("Такой буквы в слове нет!")
            set_attempt()
        print("".join(player_word))
    else:
        if " ▒" in player_word:
            print("Увы, слово отгадать Вам не удалось!")
        else:
            print("Поздравляем, Вы угадали слово!")

def game(at = 0, wrd_play = False, field = False ):
    global attempt
    attempt = at
    if field:
        print("В прошлый раз вы отгадали: ")
        word_for_play = wrd_play
        player_word = field
    else:
        word_for_play = get_word()
        player_word = get_field(word_for_play)
    print("".join(player_word))
    engine(word_for_play, player_word)

print('''
*******************************
********* ПОЛЕ ЧУДЕС **********

1. Начать игру!
2. Сохранить игру (используйте во время игры).
3. Загрузить игру.
4. Выйти.

''')

key = int(input('Ваш выбор : '))
match key:
    case 1:
        init()
        game()
    case 2:
        exit(0)
    case 3:
        for i in [i for i in os.listdir(os.getcwd()) if i[-3:] == "pkl"]:
            print(i)
        name_save = str(input("Введите имя файла: "))
        with open(name_save, 'rb') as f:
            sg = pickle.load(f)
            word_play = sg["word"]
            atmp = sg["attempt"]
            field = sg["field"]

        init()
        game(at= atmp, wrd_play= word_play, field=field)
    case _:
        exit(0)