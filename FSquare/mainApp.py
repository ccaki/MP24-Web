from flask import Flask, render_template
import pymysql
from dbConnection import Database

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Covax/about.html', content_type='application/json')




#test db connection
@app.route('/connection')
def connection():

    def db_query():
        db = Database()
        users = db.connection()

        return users

    res = db_query()

    return render_template('users.html', result=res, content_type='application/json')

