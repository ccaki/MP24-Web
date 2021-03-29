from flask import Flask, render_template,current_app
from flask import request

import pymysql
from dbConnection import Database

app = Flask(__name__)
db = Database()
# @app.route('/')
# def home():
#     return app.send_static_file('templates/Covax/about.html')

def db_query(sql):
    rs = db.get_from_table(sql)
    return rs

#home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def home1():
    return render_template('index.html')



#about-us page
@app.route('/about')
def about():
    return render_template('about1.html')

#blog page
@app.route('/precaution')
def blog():
    return render_template('blog.html')

#get detailed blog entry from database
def get_detail(category,id):
    sql = "SELECT * FROM mp24.articles WHERE category = '"+category+"' AND id = " + id
    print(sql)
    res = db_query(sql)
    #get the only element in the res list
    res = res[0]
    return res



#mask detail page
@app.route('/maskdetail/<variable>', methods=['GET'])
def maskdetail(variable):
    res = get_detail('mask',variable)
    return render_template('blog-details.html',result=res, content_type='application/json')

#hygiene detail page
@app.route('/hygienedetail/<variable>', methods=['GET'])
def hygienedetail(variable):
    res = get_detail('good hygiene',variable)
    return render_template('blog-details.html',result=res, content_type='application/json')

#travel detail page
@app.route('/traveldetail/<variable>', methods=['GET'])
def traveldetail(variable):
    res = get_detail('travel restriction',variable)
    print(res)
    return render_template('blog-details.html',result=res, content_type='application/json')

#isolation detail page
@app.route('/isolationdetail/<variable>', methods=['GET'])
def isolationdetail(variable):
    res = get_detail('isolation',variable)
    return render_template('blog-details.html',result=res, content_type='application/json')

#transmission detail page
@app.route('/transmissiondetail/<variable>', methods=['GET'])
def transmissiondetail(variable):
    res = get_detail('transmission',variable)
    return render_template('blog-details.html',result=res, content_type='application/json')

#symptom detail page
@app.route('/symptomdetail/<variable>', methods=['GET'])
def symptomdetail(variable):
    res = get_detail('symptom',variable)
    return render_template('blog-details.html',result=res, content_type='application/json')


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

#return travel restriction page
@app.route('/travel_restriction')
def travel_restriction():
    #return transmission.html
    sql = "SELECT * FROM mp24.articles WHERE category = 'travel restriction'"
    res = db_query(sql)
    #shorten the body preview
    #iterate the res list
    for dic in res:
    #iterate the dict in the res list
        for key in dic:
            if key == "body":
                dic[key] = dic[key][0:150]
    return render_template('travel.html',result=res, content_type='application/json')


#return hygiene page
@app.route('/good_hygiene')
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

#return isolation page
@app.route('/isolation')
def isolation():
    #return hygiene.html
    sql = "SELECT * FROM mp24.articles WHERE category = 'isolation'"
    res = db_query(sql)
    #shorten the body preview
    #iterate the res list
    for dic in res:
    #iterate the dict in the res list
        for key in dic:
            if key == "body":
                dic[key] = dic[key][0:150]
    return render_template('isolation.html',result=res, content_type='application/json')


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



# #vaccine page
# @app.route('/vaccine')
# def vaccine():
#     res = db_query('articles')
#     return render_template('vaccine.html',result=res, content_type='application/json')

#test page
# @app.route('/test')
# def test():
#     return render_template('test.html', content_type='application/json')