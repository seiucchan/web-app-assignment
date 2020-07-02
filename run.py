from flask import render_template, redirect, request

from app import app
import mysql.connector
from quiz_app.database import MySQL


config={'user':'root', 'host':'localhost', 'password':'Sivuch1144', 'database':'jn_lecture'}
db = MySQL(**config)

@app.route('/')
def index():
    html = render_template('index.html')

    return html

@app.route('/quizes')
def quizes():
    stmt = 'SELECT * FROM quize'
    quizes = db.query(stmt)
    html = render_template('quizes.html', quizes=quizes)

    return html

@app.route('/quizes/<int:id>')
def quize(id):
    stmt = 'SELECT * FROM quize WHERE id = ?'
    quize = db.query(stmt, id, prepared=True)
    html = render_template('quize.html',quize=quize[0])

    return html

@app.route('/answer/<int:id>')
def answer(id):
    stmt = 'SELECT * FROM quize WHERE id = ?'
    answer = db.query(stmt, id, prepared=True)
    html = render_template('answer.html',answer=answer[0])

    return html

@app.route('/input_register')
def input_register():
    html = render_template('input_register.html')

    return html

@app.route('/register', methods=["POST"])
def register():
    question = str(request.form.get('question'))
    answer = str(request.form.get('answer'))

    db.insert("INSERT INTO `quize` (`question`, `answer`) VALUES ('{question}', '{answer}');".format(question=question, answer=answer))

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=8888, threaded=True) 