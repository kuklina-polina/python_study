# user: Polina Kuklina
# date creation: 21.11.2024

#todo: Выбрать из файла db_design.pdf вариант задания. Спроектировать ER модель на сайте
# https://editor.ponyorm.com . Сгенерировать скрипт и создать схему для СУБД PostgreSQL.
# Наполнить модель данными. Написать запросы к заданию на стороне клиента python.
# Вариант 6. Кафедра

import psycopg2
import pandas as pd
from psycopg2 import Error

def print_result_sql(query, list_col_name):
    cursor.execute(query)
    df = pd.DataFrame(cursor.fetchall(), columns=list_col_name)
    print(df)
try:
    connection = psycopg2.connect(user="polina",
                                  password="polina",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="sci_dep")
    cursor = connection.cursor()

    print("___________________________")
    print("Выдавать сводную информацию обо всех работниках кафедры")
    query_employees = ('''SELECT e.id, e.lastname, e.name, e.patronymic, p.post_name, r.rank_name 
                        FROM  employees e, posts p , ranks r
                        WHERE e.post = p.id AND e.rank = r.id 
                        ORDER BY e.id''')
    print_result_sql(query_employees, ["id", "Фамилия", "Имя", "Отчество", "должность", "научное звание"])

    print("___________________________")
    print("Выдавать информацию о НИР")
    query_emp_str_info = ('''(SELECT e.id, e.lastname || ' ' || e.name || ' ' || e.patronymic ||
                            ' — ' || p.post_name || ' — ' || r.rank_name as info
                            FROM  employees e, posts p , ranks r 
                            WHERE e.post = p.id AND e."rank" = r.id 
                            ORDER BY e.id)''')
    query_researches = (f'''SELECT r.name, r."desc", array_agg(e.info) 
                        FROM employees_researches er, researches r,  {query_emp_str_info}e  
                        WHERE er.id_employee = e.id AND er.id_research = r.id
                        GROUP BY r.name, r.desc''')
    print_result_sql(query_researches, [ "Название", "Описание", "Задействованные сотрудники"])

    print("___________________________")
    print("Выдавать информацию о преподавателе, ведущего указанный вид занятий по указанной дисциплине")
    query_emp_str_info = ('''(SELECT e.id, e.lastname || ' ' || e.name || ' ' || e.patronymic ||
                            ' — ' || p.post_name || ' — ' || r.rank_name as info
                            FROM  employees e, posts p , ranks r 
                            WHERE e.post = p.id AND e."rank" = r.id 
                            ORDER BY e.id)''')
    query_researches = (f'''SELECT d.name, lt."type" , d.desc, array_agg(e.info)
                FROM disciplines d, disciplines_lestypes dl , employees_disciplines ed, lesson_types lt , {query_emp_str_info} e  
                WHERE ed.id_employee = e.id AND ed.id_discipline = dl.id  AND dl.id_discipline = d.id AND dl.id_lestype = lt.id 
                GROUP BY d.name, lt."type" , d.desc;''')
    print_result_sql(query_researches, [ "Дисциплина", "Тип занятия", "Описание дисциплины", "Задействованные сотрудники"])

    print("___________________________")
    print("Выдавать информацию о видах занятий, которые проводятся по выбранной дисциплине.")

    query_researches = (f'''SELECT d.name, lt."type" 
                        FROM disciplines d, disciplines_lestypes dl , lesson_types lt 
                        WHERE dl.id_discipline = d.id AND dl.id_lestype = lt.id
                        ORDER BY d.name, lt."type";''')
    print_result_sql(query_researches, [ "Дисциплина", "Тип занятия"])
    print("___________________________")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")