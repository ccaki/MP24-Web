from flask import Flask, render_template,current_app

import pymysql
from dbConnection import Database

app = Flask(__name__)

@app.route('/')
def home():
    return current_app.send_static_file('templates/Covax/about.html')

#test bootstrap
@app.route('/bs')
def bs():
    return render_template('bstesting.html', content_type='application/json')


#test db connection
@app.route('/connection')
def connection():

    def db_query():
        db = Database()
        users = db.connection()

        return users

    res = db_query()

    return render_template('users.html', result=res, content_type='application/json')

