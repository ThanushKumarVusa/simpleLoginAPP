import os
import pymysql


def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "login_user"),
        password=os.getenv("DB_PASSWORD", "loginpassword"),
        database=os.getenv("DB_NAME", "login_app"),
        cursorclass=pymysql.cursors.DictCursor
    )
