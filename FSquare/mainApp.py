from flask import Flask, render_template,current_app

import pymysql
from dbConnection import Database

app = Flask(__name__)

# @app.route('/')
# def home():
#     return app.send_static_file('templates/Covax/about.html')

#about-us page
@app.route('/about')
def about():
    return render_template('about.html')

#blog page
@app.route('/blog')
def blog():
    return render_template('blog.html')

#home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def home1():
    return render_template('index.html')


#test db connection
@app.route('/connection')
def connection():

    def db_query():
        db = Database()
        users = db.connection()

        return users

    res = db_query()

    return render_template('static/templates/users.html', result=res, content_type='application/json')

