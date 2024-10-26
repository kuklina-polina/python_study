# user: Polina Kuklina
# date creation: 15.10.2024

#todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html.

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}

template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">
 
  <p>?</p>

 </body>
</html>
"""

def create_fill_html_by_ques(arr, html_template, file_name):
    for key, value in arr.items():
        index_key = html_template.index(key)
        index_position = html_template[index_key:].index("?")
        html_template = html_template[:index_key + index_position] + value + html_template[index_key + index_position + 1:]
    f = open(file_name, "wt", encoding="utf-8")
    f.write(html_template)
    f.close()

create_fill_html_by_ques(page, template, "index.html")