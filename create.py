import json
import mysql.connector
from config import DB_HOST,DB_NAME,DB_PWD,DB_USER

def create_database():
    """
        create MySQL database
    """
    db = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PWD,
        database=DB_NAME
    )

    cursor = db.cursor()

    with open("spring2024.json", 'r') as file:
        courses_data = json.load(file)
    for course in courses_data:
        sql = "INSERT INTO courses (name, code, description, credit, prereq, hub) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (course['name'], course['code'], course['description'], course['credit'], course.get('prereq', None), course['hub'])
        cursor.execute(sql, val)
        
    db.commit()
    print(f"Database created or already exists.")

    cursor.close()
    db.close()

if __name__ == "__main__":
    create_database()