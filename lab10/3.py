import psycopg2

connection = None  # ← Add this to avoid NameError

try:
    # Connect to your postgres DB
    connection = psycopg2.connect(
        dbname="Example1",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )

    cursor = connection.cursor()

    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print("PostgreSQL version:", version)

except Exception as e:
    print("An error occurred:", e)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection closed.")