from flask import Flask, render_template,current_app
from flask import request

import pymysql
from dbConnection import Database

app = Flask(__name__)

# @app.route('/')
# def home():
#     return app.send_static_file('templates/Covax/about.html')

def db_query(sql):
    db = Database()
    rs = db.get_from_table(sql)
    return rs


#about-us page
@app.route('/about')
def about():
    return render_template('about1.html')

#blog page
@app.route('/blog')
def blog():
    return render_template('blog.html')

#blog detail page
@app.route('/blogdetail')
def blogdetail():
    sql = "SELECT * FROM mp24.articles WHERE category = 'mask'"
    res = db_query(sql)
    res = res[1]
    return render_template('blog-details.html',result=res, content_type='application/json')



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

#return transmission page
@app.route('/transmission')
def transmission():
    #return transmission.html
    sql = "SELECT * FROM mp24.articles WHERE category = 'transmission'"
    res = db_query(sql)
    #shorten the body preview
    #iterate the res list
    for dic in res:
    #iterate the dict in the res list
        for key in dic:
            if key == "body":
                dic[key] = dic[key][0:150]
    return render_template('transmission.html',result=res, content_type='application/json')
#read more should be renamed since other page still got rename


#return hygiene page
@app.route('/hygiene')
def hygiene():
    #return hygiene.html
    sql = "SELECT * FROM mp24.articles WHERE category = 'good hygiene'"
    res = db_query(sql)
    #shorten the body preview
    #iterate the res list
    for dic in res:
    #iterate the dict in the res list
        for key in dic:
            if key == "body":
                dic[key] = dic[key][0:150]
    return render_template('hygiene.html',result=res, content_type='application/json')

#return symptom page
@app.route('/symptom')
def symptom():
    #return hygiene.html
    sql = "SELECT * FROM mp24.articles WHERE category = 'symptom'"
    res = db_query(sql)
    #shorten the body preview
    #iterate the res list
    for dic in res:
    #iterate the dict in the res list
        for key in dic:
            if key == "body":
                dic[key] = dic[key][0:150]
    return render_template('symptom.html',result=res, content_type='application/json')


#returns mask page
@app.route('/mask')
def mask():
    sql = "SELECT * FROM mp24.articles WHERE category = 'mask'"
    res = db_query(sql)
    #shorten the body preview
    #iterate the res list
    for dic in res:
    #iterate the dict in the res list
        for key in dic:
            if key == "body":
                dic[key] = dic[key][0:150]
    return render_template('mask.html',result=res, content_type='application/json')

#returns "read more" result for blog pages
@app.route('/mask_articles/<articlenum>')
def read_more(articlenum):
    results1 = request.args.get('results1', '0-100')
    return articlenum


# #vaccine page
# @app.route('/vaccine')
# def vaccine():
#     res = db_query('articles')
#     return render_template('vaccine.html',result=res, content_type='application/json')

#test page
@app.route('/test')
def test():
    return render_template('test.html', content_type='application/json')