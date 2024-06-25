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

def insert_store(conn, store):
    try:
        sql = '''
        insert into stores(title) values(?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, store)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def insert_category(conn, category):
    try:
        sql = '''
        insert into categories(code,title) values(?,?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, category)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def insert_product(conn, product):
    try:
        sql = '''
        insert into products(title, category_code, unit_price, stock_quantity, store_id) values(?,?,?,?,?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def show_stores(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT store_id, title FROM stores')
        cities = cursor.fetchall()
        for city in cities:
            print(f"{city[0]}. {city[1]}")
    except sqlite3.Error as e:
        print(e)


def show_products_by_store_id(connection, city_id):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            SELECT  products.title,  products.unit_price, products.stock_quantity, categories.title
            FROM products 
            inner join categories ON products.category_code = categories.code
            JOIN stores ON products.store_id = stores.store_id
            WHERE stores.store_id = ?
        ''', (city_id,))
        products = cursor.fetchall()
        if products:
            print("\nproducts в выбранном store:")
            for product in products:
                print(product)
        else:
            print("В выбранном store нет product.")
    except sqlite3.Error as e:
        print(e)


category_table = """CREATE TABLE categories(
                    code VARCHAR(2) primary key ,
                    title VARCHAR(150))"""

store_table = """CREATE TABLE stores(
store_id integer primary key,
title varchar(100))"""

product_table = """CREATE TABLE products(
id INTEGER PRIMARY KEY,
title VARCHAR(255),
category_code varchar(2) references categories(code),
unit_price float,
stock_quantity integer,
store_id integer references stores(store_id))"""

con = create_connection("test.db")
if con:
    create_table(con, category_table)
    create_table(con, store_table)
    create_table(con, product_table)

    insert_category(con, ('FD', 'food product'))
    insert_category(con, ('EL', 'electronics'))
    insert_category(con, ('CL', 'clothes'))

    insert_store(con, ('asia',))
    insert_store(con, ('globus',))
    insert_store(con, ('spar',))

    insert_product(con, ('chocolate', 'FD', 10.5, 129, 1))
    insert_product(con, ('jeans', 'CL', 120.0, 55, 2))
    insert_product(con, ('t-shirt', 'CL', 0.0, 15, 1))

    while True:
        print("\nВы можете отобразить список products, выбрав ID store:")
        show_stores(con)
        try:
            store_id = int(input("Введите ID store (0 для выхода): "))
            if store_id == 0:
                break
            elif 1 <= store_id <= 3:
                show_products_by_store_id(con,store_id)
            else:
                print("Неверный ID store. Пожалуйста, повторите попытку.")
        except ValueError:
            print("Неверный ввод. Введите корректный ID store.")

    print("good")
