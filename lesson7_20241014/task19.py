# user: Polina Kuklina
# date creation: 15.10.2024

#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# – id - номер по порядку (от 1 до 10);
# – текст из списка algoritm

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]
#
# Каждое значение из списка должно находится на отдельной строке.
# Выход:
# 1 % "C4.5"
# 2 % "k - means"
# и т.д.

def create_csv_file(list_input, name_csv):
    f = open(name_csv, "wt", encoding="utf-8")
    for key in range(len(list_input)):
        f.write(f"{key+1} % \"{list_input[key]}\"\n")
    f.close()

create_csv_file(algoritm, "algoritm.csv")