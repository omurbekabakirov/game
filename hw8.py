import sqlite3


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_country(conn, title):
    try:
        sql = '''
        insert into country(title) values(?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, title)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def insert_city(conn, title):
    try:
        sql = '''
        insert into city(title,area,country_id) values(?,?,?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, title)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def insert_student(connection, students):
    sql = '''INSERT INTO student (first_name,last_name, city_id) VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, students)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def show_cities(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT id, title FROM city')
        cities = cursor.fetchall()
        for city in cities:
            print(f"{city[0]}. {city[1]}")
    except sqlite3.Error as e:
        print(e)


def show_students_by_city(connection, city_id):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            SELECT student.first_name, student.last_name, country.title, city.title, city.area
            FROM student
            JOIN city ON student.city_id = city.id
            JOIN country ON city.country_id = country.id
            WHERE city.id = ?
        ''', (city_id,))
        students = cursor.fetchall()
        if students:
            print("\nСтуденты в выбранном городе:")
            for student in students:
                print(f"Имя: {student[0]} {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь: {student[4]}")
        else:
            print("В выбранном городе нет студентов.")
    except sqlite3.Error as e:
        print(e)



country_table = '''
                create table country(
                            id integer primary key autoincrement ,
                            title text not null 
                    )
                '''

city_table = '''
                create table city(
                            id integer primary key autoincrement ,
                            title text not null,
                            area float default 0,
                            country_id INTEGER REFERENCES country(id) ON DELETE CASCADE
                    )
                '''

student_table = '''
                create table student(
                            id integer primary key autoincrement ,
                            first_name text not null,
                            last_name text not null,
                            city_id INTEGER REFERENCES city(id) ON DELETE CASCADE
                    )
                '''


connection = create_connection('hw8.db')


if connection:
    print('Connection successful')

    create_table(connection, country_table)
    create_table(connection, city_table)
    create_table(connection, student_table)

    insert_country(connection, ('UK', ))
    insert_country(connection, ('Japan', ))
    insert_country(connection, ('Russia', ))

    insert_city(connection, ('London', 500, 1))
    insert_city(connection, ('Bradford', 450, 1))
    insert_city(connection, ('Osaka', 350, 2))
    insert_city(connection, ('Tokyo', 550, 2))
    insert_city(connection, ('Moscow', 750, 3))
    insert_city(connection, ('Peter Burg', 650, 3))
    insert_city(connection, ('Sevastopol', 430, 3))

    insert_student(connection, ('Max', 'Koralov', 1))
    insert_student(connection, ('Petr', '1', 2))
    insert_student(connection, ('Adolf', 'Gitler', 3))
    insert_student(connection, ('Cris', 'Cris', 4))
    insert_student(connection, ('Oma', 'Abakirov', 5))
    insert_student(connection, ('Dima', 'Soikin', 6))
    insert_student(connection, ('Sasha', 'Pavlova', 7))
    insert_student(connection, ('Kiril', 'Karpov', 3))
    insert_student(connection, ('Kenpachi', 'Zarraki', 7))
    insert_student(connection, ('Masha', 'Koralova', 1))
    insert_student(connection, ('Dasha', 'Koralova', 1))
    insert_student(connection, ('Grisha', 'Koralova', 2))
    insert_student(connection, ('Natasha', 'Koralova', 3))
    insert_student(connection, ('Sophia', 'Koralova', 4))
    insert_student(connection, ('Frank', 'Djonson', 7))

    while True:
        print("\nВы можете отобразить список студентов, выбрав ID города:")
        show_cities(connection)
        try:
            city_id = int(input("Введите ID города (0 для выхода): "))
            if city_id == 0:
                break
            elif 1 <= city_id <= 7:
                show_students_by_city(connection, city_id)
            else:
                print("Неверный ID города. Пожалуйста, повторите попытку.")
        except ValueError:
            print("Неверный ввод. Введите корректный ID города.")

    connection.close()


