from flask import Flask, render_template,current_app

import pymysql
from dbConnection import Database

app = Flask(__name__)

# @app.route('/')
# def home():
#     return app.send_static_file('templates/Covax/about.html')

def db_query(tablename):
    db = Database()
    rs = db.get_table(tablename)
    return rs


#about-us page
@app.route('/about')
def about():
    return render_template('about.html')

#blog page
@app.route('/blog')
def blog():
    return render_template('blog.html')

#blog detail page
@app.route('/blogdetail')
def blogdetail():
    return render_template('blog-details.html')


#home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def home1():
    return render_template('index.html')


# #test db connection
# @app.route('/connection')
# def connection():
#
# #     def db_query():
# #         db = Database()
# #         users = db.connection()
# #
# #         return users
#
#     res = db_query('maskarticles')
#
#     return render_template('testing.html', result=res, content_type='application/json')

#mask page
@app.route('/mask')
def mask():
    res = db_query('articles')
    return render_template('mask.html',result=res, content_type='application/json')