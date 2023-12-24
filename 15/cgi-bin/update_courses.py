#!/usr/bin/env python
import cgi
import sqlite3

print("Content-type: text/html\n")  # Заголовок HTTP-ответа

form = cgi.FieldStorage()

# Устанавливаем соединение с базой данных
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Обработка данных из формы и обновление информации в базе данных
if form.getvalue('course_id') and (form.getvalue('course_name') or form.getvalue('instructor_id')):
    course_id = form.getvalue('course_id')
    course_name = form.getvalue('course_name')
    instructor_id = form.getvalue('instructor_id')

    # Обновление данных в таблице Courses
    if course_name:
        cursor.execute("UPDATE Courses SET CourseName = ? WHERE CourseID = ?", (course_name, course_id))
    if instructor_id:
        cursor.execute("UPDATE Courses SET InstructorID = ? WHERE CourseID = ?", (instructor_id, course_id))

    conn.commit()

# HTML форма для ввода данных
print('''
<!DOCTYPE html>
<html lang="ru">
<head>
    <title>БД</title>
    <meta charset="UTF-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
</head>
<body>
    <h1>Обновление информации о курсах</h1>
    <form method="post" action="">
        <label for="course_id">ID Курса:</label><br>
        <input type="text" id="course_id" name="course_id"><br><br>

        <label for="course_name">Новое название курса:</label><br>
        <input type="text" id="course_name" name="course_name"><br><br>

        <label for="instructor_id">Новый ID преподавателя:</label><br>
        <input type="text" id="instructor_id" name="instructor_id"><br><br>

        <input class="btn btn-danger" type="submit" value="Обновить информацию">
    </form>
</body>
</html>
''')

conn.close()