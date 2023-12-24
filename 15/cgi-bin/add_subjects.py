import cgi
import cgitb
import codecs
import html
import sys

from db import add_subjects

cgitb.enable()

form = cgi.FieldStorage()

subjects = html.escape(form.getvalue('field-subjects'))

add_subjects(name=subjects)

print("Content-type: text/html")
print(f'''
        <!DOCTYPE html>
        <html lang="ru">
            <head>
                <title>БД</title>
                <meta charset="UTF-8">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
            </head>
            <body>
                <h1> Предмет {subjects} успешно добавлен </h1><br>
                <a class="btn btn-success" href="../templates/index.html">На главную</a><br>
            </body>
        </html>
''')
