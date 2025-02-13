from database import get_db_connection
from schemas import UserCreate
from schemas import ResCreate

# Create a new user
def create_user(user: UserCreate):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.execute(sql, (user.name, user.email))
        connection.commit()
        user_id = cursor.lastrowid
    connection.close()
    return {"id": user_id, **user.model_dump()}

# Read all users
def get_users():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    connection.close()
    return users

# Read a single user by ID
def get_user(user_id: int):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
    connection.close()
    return user

# Update a user
def update_user(user_id: int, user: UserCreate):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
        cursor.execute(sql, (user.name, user.email, user_id))
        connection.commit()
    connection.close()
    return {"id": user_id, **user.model_dump()}

# Delete a user
def delete_user(user_id: int):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        connection.commit()
    connection.close()
    return {"message": "User deleted successfully"}

def create_res(res_link : ResCreate):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO restaurants_link (link) VALUES (%s)"
        cursor.execute(sql, (res_link.link,))
        connection.commit()
        res_id = cursor.lastrowid
    connection.close()
    return {'id': res_id, **res_link.model_dump()}

