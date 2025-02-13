# Database Configuration
import pymysql

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "actowiz",
    "database": "fast_api",
    "cursorclass": pymysql.cursors.DictCursor
}

# Create a database connection
def get_db_connection():
    connection = pymysql.connect(**DB_CONFIG)
    return connection
