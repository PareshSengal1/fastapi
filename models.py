import pymysql
from database import get_db_connection

def create_table():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        )
        """)
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS restaurants_link (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    link VARCHAR(500) UNIQUe NOT NULL,
                    status VARCHAR(10) DEFAULT 'pending'
                )
                """)
    connection.commit()
    connection.close()

# Run table creation when the script runs
create_table()
