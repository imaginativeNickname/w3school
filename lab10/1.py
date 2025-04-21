import psycopg2
from psycopg2 import Error
import csv

def create_database():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="123",
                                      host="localhost",
                                      port="5432")
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE phonebook_db WITH ENCODING 'UTF8'")
    except Error as e:
        print("Ошибка при создании базы данных:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

def create_table():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="123",
                                      host="localhost",
                                      port="5432",
                                      database="phonebook_db")
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS PhoneBook (
                fname TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE
            )
        """)
        connection.commit()
    except Error as e:
        print("Ошибка при создании таблицы:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

def connect_db():
    return psycopg2.connect(user="postgres",
                            password="123",
                            host="localhost",
                            port="5432",
                            database="phonebook_db")

def insert_from_csv():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        with open('file.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader) 
            for row in reader:
                cursor.execute("INSERT INTO PhoneBook (fname, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING", row)
        connection.commit()
    except Error as e:
        print("Ошибка при добавлении из CSV:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

def insert_manually():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        name = input("Введите имя: ")
        phone = input("Введите номер: ")
        cursor.execute("INSERT INTO PhoneBook (fname, phone) VALUES (%s, %s)", (name, phone))
        connection.commit()
    except Error as e:
        print("Ошибка при добавлении контакта:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

def update_contact():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        choice = int(input("Обновить имя (1) или номер (2)?: "))
        if choice == 1:
            phone = input("Введите номер, для которого нужно изменить имя: ")
            new_name = input("Введите новое имя: ")
            cursor.execute("UPDATE PhoneBook SET fname=%s WHERE phone=%s", (new_name, phone))
        elif choice == 2:
            name = input("Введите имя, для которого нужно изменить номер: ")
            new_phone = input("Введите новый номер: ")
            cursor.execute("UPDATE PhoneBook SET phone=%s WHERE fname=%s", (new_phone, name))
        connection.commit()
    except Error as e:
        print("Ошибка при обновлении контакта:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

def get_contacts():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        choice = int(input("Фильтр по имени (1) или номеру (2)?: "))
        if choice == 1:
            name = input("Введите имя: ")
            cursor.execute("SELECT * FROM PhoneBook WHERE fname=%s", (name,))
        else:
            phone = input("Введите номер: ")
            cursor.execute("SELECT * FROM PhoneBook WHERE phone=%s", (phone,))
        print(cursor.fetchall())
    except Error as e:
        print("Ошибка при получении данных:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

def delete_contact():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        choice = int(input("Удалить по имени (1) или номеру (2)?: "))
        if choice == 1:
            name = input("Введите имя: ")
            cursor.execute("DELETE FROM PhoneBook WHERE fname=%s", (name,))
        else:
            phone = input("Введите номер: ")
            cursor.execute("DELETE FROM PhoneBook WHERE phone=%s", (phone,))
        connection.commit()
    except Error as e:
        print("Ошибка при удалении контакта:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

def main():
    create_database()
    create_table()
    while True:
        print("1 - Добавить из CSV\n2 - Ввести вручную\n3 - Обновить\n4 - Получить данные\n5 - Удалить\n6 - Выйти")
        choice = int(input("Выберите действие: "))
        if choice == 1:
            insert_from_csv()
        elif choice == 2:
            insert_manually()
        elif choice == 3:
            update_contact()
        elif choice == 4:
            get_contacts()
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            break
        else:
            print("Неверный ввод, попробуйте снова!")

main()
