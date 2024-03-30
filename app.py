from flask import Flask, render_template, request, redirect, url_for
import config

app = Flask(__name__)

@app.route('/')
def index():
    db = config.mydb()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM courses_db WHERE UPPER(code) LIKE '%CS%'")
    data = cursor.fetchall()
    return render_template('index.html', courses=data)

if __name__ == '__main__':
    app.run(debug=True)