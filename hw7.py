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


def insert_product(conn, product):
    try:
        sql = '''
        insert into products(product_title, price, quantity) values(?,?,?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def change_product_quantity(conn, product):
    try:
        sql = '''
                update products set quantity = ? where id = ?
                '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def change_product_price(conn, product):
    try:
        sql = '''
                update products set price = ? where id = ?
                '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(conn, id):
    try:
        sql = '''
                delete from products where id = ?
                '''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_product(conn):
    try:
        sql = '''
                select * from products 
                '''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_product_by_price_and_quantity(conn):
    try:
        sql = '''
                select * from products where price < 100 and  quantity > 5
                '''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_product_by_title(conn, product_title):
    try:
        sql = '''
                select * from products where product_title LIKE ?
                '''
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + product_title + '%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


product_table = '''
                create table products (
                            id integer primary key autoincrement ,
                            product_title varchar(200) not null,
                            price float(8,2) not null default 0.0,
                            quantity integer not null default 0
                    )
                '''

connection = create_connection('hw.db')

if connection:
    print('Connection successful')
    # create_table(connection, product_table)
    # insert_product(connection, ('potato', 35.0, 150))
    # insert_product(connection, ('tomato', 125.0, 50))
    # insert_product(connection, ('apple', 70.0, 40))
    # insert_product(connection, ('peach', 135.0, 25))
    # insert_product(connection, ('pineapple', 170.0, 150))
    # insert_product(connection, ('mandarin', 235.0, 250))
    # insert_product(connection, ('orange', 65.0, 110))
    # insert_product(connection, ('watermelon', 25.0, 150))
    # insert_product(connection, ('cucumber', 75.0, 120))
    # insert_product(connection, ('chili', 25.0, 150))
    # insert_product(connection, ('onion', 35.0, 80))
    # insert_product(connection, ('cabbage', 35.0, 150))
    # insert_product(connection, ('banana', 115.0, 90))
    # insert_product(connection, ('melon', 55.0, 100))
    # insert_product(connection, ('red onion', 45.0, 70))
    change_product_quantity(connection, (200, 5))
    change_product_price(connection, (250, 2))
    delete_product(connection, 4)
    select_product(connection)
    print("/")
    select_product_by_price_and_quantity(connection)
    print("/")
    select_product_by_title(connection, 'tomato')
    connection.close()
