import mysql.connector

DB_HOST = "localhost"
DB_USER = "root"
DB_PWD = ""
DB_NAME = "courses_db"

def mydb():
    """
        Provide connection to the MySQL database.
    """
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "courses_db"
    )