# user: Polina Kuklina
# date creation: 10.10.2024
# todo: База данных пользователя.
# Задан массив объектов пользователя
users_list = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fёdor', 'age': 13, 'group': "guest"}]
# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.
# Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
# тип сортировки: 1
# #Затем сообщение для ввода
# Ввидите критерии поиска: 16
# Результат:
# #Пользователь: 'Piter' возраст 23 года , группа  "admin"
# #Пользователь: 'Dasha' возраст 30 лет , группа  "master"

type_sort = int(input("Отсортировать можно по: \n1. По возрасту;\n2. По первой букве логина;\n3. По группе."
                       "\nВведите цифру - тип сортировки: "))
criteria = input("Введите критерий поиска: ")


users_new = []
if type_sort == 1:
    for ind in range(len(users_list)):
        if list(users_list[ind].items())[1][1] > int(criteria):
            users_new += [list(users_list[ind].items())]
elif type_sort == 2:
    for ind in range(len(users_list)):
        if list(users_list[ind].items())[0][1][0] == criteria:
            users_new += [list(users_list[ind].items())]
elif type_sort == 3:
    for ind in range(len(users_list)):
        if list(users_list[ind].items())[2][1] == criteria:
            users_new += [list(users_list[ind].items())]
if len(users_new) > 0:
    for i in range(len(users_new)):
        print(f"Пользователь: {users_new[i][0][1]} возраст {users_new[i][1][1]} лет, группа {users_new[i][2][1]}")
else:
    print("По вашим критериям не было найдено пользователей")
