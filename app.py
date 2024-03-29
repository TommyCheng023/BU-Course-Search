from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)

@app.route('/')
def index():
    cursor = mysql.connector.connect(**DB_CONFIG).cursor()
    cursor.execute("SELECT * FROM courses_db WHERE UPPER(code) LIKE '%CS%'")
    data = cursor.fetchall()
    return render_template('index.html', courses=data)

if __name__ == '__main__':
    app.run(debug=True)