import os
import pymysql
from urllib.parse import urlparse

# Fetch the DATABASE_URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    db_url = urlparse(DATABASE_URL)
    DB_CONFIG = {
        "host": db_url.hostname,
        "user": db_url.username,
        "password": db_url.password,
        "database": db_url.path.lstrip("/"),
        "port": db_url.port or 3306,  # Default MySQL port
        "cursorclass": pymysql.cursors.DictCursor
    }
else:
    # Local development settings
    DB_CONFIG = {
        "host": "localhost",
        "user": "root",
        "password": "actowiz",
        "database": "fast_api",
        "cursorclass": pymysql.cursors.DictCursor
    }

# Create a database connection
def get_db_connection():
    return pymysql.connect(**DB_CONFIG)
