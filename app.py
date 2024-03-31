from flask import Flask, render_template, request, redirect, url_for
import config

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    data = []
    num = 0
    db = config.mydb()
    cursor = db.cursor()

    keycode = request.args.get('content', '')
    if keycode:
        cursor.execute('SELECT * FROM courses_db WHERE code = %s', (keycode, ))
        data = cursor.fetchall()
        num = len(data)

    cursor.close()
    db.close()
    return render_template('index.html', number=num, courses=data, searchHistory=keycode)
    

if __name__ == '__main__':
    app.run(debug=True)