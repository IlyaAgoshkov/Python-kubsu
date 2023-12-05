import sqlite3

def sqlite_connection(func):
    def wrapper(*args, **kwargs):
        with sqlite3.connect('computer_courses.db') as con:
            kwargs['con'] = con
            res = func(*args, **kwargs)
            con.commit()
        return res
    return wrapper

@sqlite_connection
def drop_tables(table_names: list, con: sqlite3.Connection):
    cur = con.cursor()
    for table_name in table_names:
        cur.execute(f"DROP TABLE IF EXISTS {table_name};")
        print(f"Table '{table_name}' has been dropped successfully.")


@sqlite_connection
def init_db(con: sqlite3.Connection):
    cur = con.cursor()

    # Таблица для слушателей
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Attendees (
            AttendeeID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            Name TEXT,
            Email TEXT,
            Age INTEGER
        );
    """)

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

    # Таблица для журнала успеваемости
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PerformanceJournal (
            RecordID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            AttendeeID INTEGER,
            CourseID INTEGER,
            SubjectID INTEGER,
            Grade INTEGER,
            FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID),
            FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
            FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID)
        );
    """)

@sqlite_connection
def select_data_from_table(con: sqlite3.Connection):
    cur = con.cursor()

    # Выборка данных из таблицы слушателей (Attendees)
    cur.execute("SELECT * FROM Attendees;")
    attendees_data = cur.fetchall()
    print("Attendees:")
    for attendee in attendees_data:
        print(attendee)

    # Выборка данных из таблицы курсов (Courses)
    cur.execute("SELECT * FROM Courses;")
    courses_data = cur.fetchall()
    print("\nCourses:")
    for course in courses_data:
        print(course)

    # Выборка данных из таблицы предметов (Subjects)
    cur.execute("SELECT * FROM Subjects;")
    subjects_data = cur.fetchall()
    print("\nSubjects:")
    for subject in subjects_data:
        print(subject)

    # Выборка данных из таблицы преподавателей (Instructors)
    cur.execute("SELECT * FROM Instructors;")
    instructors_data = cur.fetchall()
    print("\nInstructors:")
    for instructor in instructors_data:
        print(instructor)

    # Выборка данных из таблицы журнала успеваемости (PerformanceJournal)
    cur.execute("SELECT * FROM PerformanceJournal;")
    performance_data = cur.fetchall()
    print("\nPerformance Journal:")
    for record in performance_data:
        print(record)


@sqlite_connection
def select_attendee_by_email(email: str, con: sqlite3.Connection):
    """
    Выбирает слушателя по адресу электронной почты.
    """
    cur = con.cursor()
    cur.execute("SELECT * FROM Attendees WHERE Email = ?;", (email,))
    return cur.fetchone()

@sqlite_connection
def update_course_name(course_id: int, new_name: str, con: sqlite3.Connection):
    """
    Обновляет название курса по его идентификатору.
    """
    cur = con.cursor()
    cur.execute("UPDATE Courses SET CourseName = ? WHERE CourseID = ?;", (new_name, course_id))
    con.commit()

@sqlite_connection
def delete_subject(subject_name: str, con: sqlite3.Connection):
    """
    Удаляет предмет по его названию.
    """
    cur = con.cursor()
    cur.execute("DELETE FROM Subjects WHERE SubjectName = ?;", (subject_name,))
    con.commit()

@sqlite_connection
def join_attendee_course(con: sqlite3.Connection):
    """
    Выполняет объединение таблиц Attendees и Courses.
    """
    cur = con.cursor()
    cur.execute("""
        SELECT A.Name AS AttendeeName, C.CourseName
        FROM Attendees A
        JOIN PerformanceJournal P ON A.AttendeeID = P.AttendeeID
        JOIN Courses C ON P.CourseID = C.CourseID;
    """)
    return cur.fetchall()


@sqlite_connection
def select_instructor_id_by_name(instructor_name: str, con: sqlite3.Connection):
    """
    Выбирает идентификатор преподавателя по его имени и выводит результаты в консоль.
    """
    cur = con.cursor()
    cur.execute("SELECT InstructorID FROM Instructors WHERE InstructorName = ?;", (instructor_name,))
    data = cur.fetchone()

    if data:
        print("Найден ID инструктора:")
        print(data)
    else:
        print("ID инструктора не найдено")

@sqlite_connection
def update_attendee_email(old_email: str, new_email: str, con: sqlite3.Connection):
    """
    Обновляет адрес электронной почты слушателя.
    """
    cur = con.cursor()
    cur.execute("UPDATE Attendees SET Email = ? WHERE Email = ?;", (new_email, old_email))
    con.commit()

@sqlite_connection
def delete_instructor_by_email(email: str, con: sqlite3.Connection):
    """
    Удаляет преподавателя по адресу электронной почты.
    """
    cur = con.cursor()
    cur.execute("DELETE FROM Instructors WHERE Email = ?;", (email,))
    con.commit()


@sqlite_connection
def select_subjects_by_attendee_id(attendee_id: int, con: sqlite3.Connection):
    """
    Выбирает предметы, изучаемые слушателем по его идентификатору и выводит результаты в консоль.
    """
    cur = con.cursor()
    cur.execute("""
        SELECT S.SubjectName
        FROM Subjects S
        JOIN PerformanceJournal P ON S.SubjectID = P.SubjectID
        WHERE P.AttendeeID = ?;
    """, (attendee_id,))
    data = cur.fetchall()

    if data:
        print(f"Предметы, изучаемые слушателем {attendee_id}:")
        for subject in data:
            print(subject)
    else:
        print("Темы для этого участника не найдены.")


@sqlite_connection
def insert_new_instructor(name: str, email: str, con: sqlite3.Connection):
    """
    Добавляет нового преподавателя в базу данных.
    """
    cur = con.cursor()
    cur.execute("INSERT INTO Instructors (InstructorName, Email) VALUES (?, ?);", (name, email))
    con.commit()

@sqlite_connection
def delete_course(course_id: int, con: sqlite3.Connection):
    """
    Удаляет курс по его идентификатору.
    """
    cur = con.cursor()
    cur.execute("DELETE FROM Courses WHERE CourseID = ?;", (course_id,))
    con.commit()


@sqlite_connection
def select_attendees_by_course(course_id: int, con: sqlite3.Connection):
    """
    Выбирает слушателей курса по его идентификатору и выводит результаты в консоль.
    """
    cur = con.cursor()
    cur.execute("""
        SELECT A.Name
        FROM Attendees A
        JOIN PerformanceJournal P ON A.AttendeeID = P.AttendeeID
        WHERE P.CourseID = ?;
    """, (course_id,))
    data = cur.fetchall()

    if data:
        print(f"Слушатели курса c ID {course_id}:")
        for attendee in data:
            print(attendee)
    else:
        print("Для этого курса не найдено слушателей.")


if __name__ == '__main__':
    # init_db()
    # insert_initial_data()
    select_data_from_table()

    # Вызов функций для работы с базой данных
    select_attendee_by_email('ivanov@example.com')
    update_course_name(1, 'Advanced Programming')
    delete_subject('JavaScript')
    join_attendee_course()
    select_instructor_id_by_name('Александр Сергеевич')
    update_attendee_email('ivanov@example.com', 'ivan@example.com')
    delete_instructor_by_email('elena@example.com')
    select_subjects_by_attendee_id(1)
    insert_new_instructor('Новый Инструктор', 'new_instructor@example.com')
    delete_course(2)
    select_attendees_by_course(1)