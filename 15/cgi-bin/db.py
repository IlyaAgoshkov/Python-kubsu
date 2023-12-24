import sqlite3
from typing import Dict, List

"""Тема таблиц курсы"""

def sqlite_connection(func):
    def wrapper(*args, **kwargs):
        with sqlite3.connect('db.db') as con:
            kwargs['con'] = con
            res = func(*args, **kwargs)
            con.commit()
        return res
    return wrapper


@sqlite_connection
def init_db(con: sqlite3.Connection):
    """Создаём таблицу с id, цвет,  выдержкой, сортом, страной, описанием вина"""
    cur = con.cursor()
    # Таблица для курсов
    cur.execute("""
           CREATE TABLE IF NOT EXISTS Courses (
               CourseID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               CourseName TEXT,
               InstructorID INTEGER,
               FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID)
           );
       """)

    # Таблица для предметов
    cur.execute("""
           CREATE TABLE IF NOT EXISTS Subjects (
               SubjectID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               SubjectName TEXT
           );
       """)

    # Таблица для преподавателей
    cur.execute("""
           CREATE TABLE IF NOT EXISTS Instructors (
               InstructorID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               InstructorName TEXT,
               Email TEXT
           );
       """)
    cur.execute("INSERT INTO Courses (CourseName, InstructorID) VALUES ('Математика', 1),('Физика', 2),('Программирование', 3);")
    cur.execute("INSERT INTO Subjects (SubjectName) VALUES ('Алгебра'),('Физика ЭВМ'),('Python');")
    cur.execute("INSERT INTO Instructors (InstructorName, Email) VALUES ('Pr. Лапина', 'lap@gmail.com'),('Prof. Рубцов', 'rub@gmail.com'),('Mr Шиян', 'shiyan@gmail.com');")


@sqlite_connection
def get_all_courses(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
        SELECT CourseID, CourseName, InstructorName
        FROM Courses
        LEFT JOIN Instructors ON Courses.InstructorID = Instructors.InstructorID;
    ''')
    return cur.fetchall()

@sqlite_connection
def get_all_subjects(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
        SELECT SubjectID, SubjectName
        FROM Subjects;
    ''')
    return cur.fetchall()

@sqlite_connection
def get_all_instructors(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
        SELECT InstructorID, InstructorName, Email
        FROM Instructors;
    ''')
    return cur.fetchall()

@sqlite_connection
def add_courses(con: sqlite3.Connection, SubjectName: str, id: int):
    cur = con.cursor()
    cur.execute('''
        INSERT INTO Courses (SubjectName, InstructorName) VALUES (?, ?);
    ''', (SubjectName, id))


@sqlite_connection
def add_subjects(con: sqlite3.Connection, name: str):
    cur = con.cursor()
    cur.execute('''
        INSERT INTO Subjects (SubjectName) VALUES (?);
    ''', (name,))


def update_courses(con: sqlite3.Connection, name: str, id: int):
    cur = con.cursor()
    cur.execute('''
        UPDATE Courses
        SET CourseName = (?)
        WHERE InstructorID = (?)
    ''', (name, id))


def delete_courses(con: sqlite3.Connection, id: int):
    cur = con.cursor()
    cur.execute('DELETE FROM Courses WHERE InstructorID = (?)', (id,))


@sqlite_connection
def add_instructor(con: sqlite3.Connection, name: str, email: str):

    cur = con.cursor()
    cur.execute("INSERT INTO Instructors (InstructorName, Email) VALUES (?, ?);", (name, email))

@sqlite_connection
def update_course_name(course_id: int, new_name: str, con: sqlite3.Connection):
    """
    Обновляет название курса по его идентификатору.
    """
    cur = con.cursor()
    cur.execute("UPDATE Courses SET CourseName = ? WHERE CourseID = ?;", (new_name, course_id))

if __name__ == '__main__':
    init_db()
