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

#precaution page
@app.route('/precaution')
def precaution():
    return render_template('precaution.html')

#fact page
@app.route('/fact')
def fact():
    return render_template('fact.html')


#get detailed blog entry from database
def get_detail(category,id):
    sql = "SELECT * FROM fsquare.articles WHERE category = '"+category+"' AND id = " + id
    print(sql)
    res = db_query(sql)
    #get the only element in the res list
    res = res[0]
    return res


#determine if the blog has its previous or next blog of the same kind
def return_blog_detail(id,category,res):
    #Check if this is the last blog of this kind
    sql = "SELECT * FROM fsquare.articles WHERE category = '"+category+"' AND id >= "+str(id)
    #print(sql)
    bigger = db_query(sql)

    #if this is the only blog of this kind
    if(len(bigger)==1):
        sql = "SELECT * FROM fsquare.articles WHERE category = '"+category+"'"
        res = db_query(sql)
        res = res[0]

        if (res['videoUrl'])!=None:
            return ('blog-details-with-video-only.html',res)
        else:
            return ('blog-details-only.html',res)

    #if this is the last blog of this kind
    if(len(bigger)<2):
        sql = "SELECT * FROM fsquare.articles WHERE category = '"+category+"'"
        res = db_query(sql)
        res = res[0]

        if (res['videoUrl'])!=None:
            return ('blog-details-with-video-last.html',res)
        else:
            return ('blog-details-last.html',res)

    #Check if this is the first blog of this kind
    sql = "SELECT * FROM fsquare.articles WHERE category = '"+category+"' AND id <= "+str(id)
    smaller = db_query(sql)

    #if this is the first blog of this kind
    if(len(smaller)<2):
        sql = "SELECT * FROM fsquare.articles WHERE category = '"+category+"'"
        res = db_query(sql)
        res = res[0]

        if (res['videoUrl'])!=None:
            return ('blog-details-with-video-first.html',res)
        else:
            return ('blog-details-first.html',res)

    #check if there is video in this blog
    if (res['videoUrl'])!=None:
        return ('blog-details-with-video.html',res)
    else:
        return ('blog-details.html',res)

#mask detail page
@app.route('/maskdetail/<variable>', methods=['GET'])
def maskdetail(variable):
    res = get_detail('mask',variable)
    id = res['id']
    category = res['category']
    output,res = return_blog_detail(id, category,res)
    return render_template(output,result=res, content_type='application/json')

#hygiene detail page
@app.route('/hygienedetail/<variable>', methods=['GET'])
def hygienedetail(variable):
    res = get_detail('good hygiene',variable)
    id = res['id']
    category = res['category']
    output,res = return_blog_detail(id, category,res)
    return render_template(output,result=res, content_type='application/json')

#travel detail page
@app.route('/traveldetail/<variable>', methods=['GET'])
def traveldetail(variable):
    res = get_detail('travel restriction',variable)
    id = res['id']
    category = res['category']
    output,res = return_blog_detail(id, category,res)
    return render_template(output,result=res, content_type='application/json')


#isolation detail page
@app.route('/isolationdetail/<variable>', methods=['GET'])
def isolationdetail(variable):
    res = get_detail('isolation',variable)
    id = res['id']
    category = res['category']
    output,res = return_blog_detail(id, category,res)
    return render_template(output,result=res, content_type='application/json')



# #isolation detail page
# @app.route('/isolationdetail/<variable>', methods=['GET'])
# def isolationdetail(variable):
#     res = get_detail('isolation',variable)
#     id = res['id']
#     category = res['category']
#
#     #Check if this is the last blog of this kind
#     sql = "SELECT * FROM fsquare.articles WHERE category = '"+category+"' AND id >= "+str(variable)
#     bigger = db_query(sql)
#
#     #if this is the last blog of this kind
#     if(len(bigger)<2):
#         sql = "SELECT * FROM fsquare.articles WHERE category = '"+category+"'"
#         res = db_query(sql)
#         res = res[0]
#
#         if (res['videoUrl'])!=None:
#             return render_template('blog-details-with-video-last.html',result=res, content_type='application/json')
#         else:
#             return render_template('blog-details-last.html',result=res, content_type='application/json')
#
#     #Check if this is the first blog of this kind
#     sql = "SELECT * FROM fsquare.articles WHERE category = '"+category+"' AND id <= "+str(variable)
#     smaller = db_query(sql)
#
#     #if this is the first blog of this kind
#     if(len(smaller)<2):
#         sql = "SELECT * FROM fsquare.articles WHERE category = '"+category+"'"
#         res = db_query(sql)
#         res = res[0]
#
#         if (res['videoUrl'])!=None:
#             return render_template('blog-details-with-video-first.html',result=res, content_type='application/json')
#         else:
#             return render_template('blog-details-first.html',result=res, content_type='application/json')
#
#
#     #check if there is video in this blog
#     if (res['videoUrl'])!=None:
#         return render_template('blog-details-with-video.html',result=res, content_type='application/json')
#     else:
#         return render_template('blog-details.html',result=res, content_type='application/json')
#

#transmission detail page
@app.route('/transmissiondetail/<variable>', methods=['GET'])
def transmissiondetail(variable):
    res = get_detail('transmission',variable)
    id = res['id']
    category = res['category']
    output,res = return_blog_detail(id, category,res)
    return render_template(output,result=res, content_type='application/json')

#symptom detail page
@app.route('/symptomdetail/<variable>', methods=['GET'])
def symptomdetail(variable):
    res = get_detail('symptom',variable)
    id = res['id']
    category = res['category']
    output,res = return_blog_detail(id, category,res)
    return render_template(output,result=res, content_type='application/json')

#vaccine detail page
@app.route('/vaccinedetail/<variable>', methods=['GET'])
def vaccinedetail(variable):
    # for the only one special article
    if (str(variable)=='26'):
        sql = "SELECT * FROM fsquare.articles WHERE category = 'vaccine' AND id = " + '26'
        res = db_query(sql)
        res=res[0]
        return render_template('blog-details-26.html', result=res, content_type='application/js')
    res = get_detail('vaccine',variable)
    id = res['id']
    category = res['category']
    output,res = return_blog_detail(id, category,res)
    return render_template(output,result=res, content_type='application/json')

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
    sql = "SELECT * FROM fsquare.articles WHERE category = 'transmission'"
    res = db_query(sql)
    return render_template('transmission.html',result=res, content_type='application/json')

#return travel restriction page
@app.route('/travel_restriction')
def travel_restriction():
    sql = "SELECT * FROM fsquare.articles WHERE category = 'travel restriction'"
    res = db_query(sql)
    return render_template('travel.html',result=res, content_type='application/json')


#return hygiene page
@app.route('/good_hygiene')
def hygiene():
    sql = "SELECT * FROM fsquare.articles WHERE category = 'good hygiene'"
    res = db_query(sql)
    return render_template('hygiene.html',result=res, content_type='application/json')

#return symptom page
@app.route('/symptom')
def symptom():
    sql = "SELECT * FROM fsquare.articles WHERE category = 'symptom'"
    res = db_query(sql)
    return render_template('symptom.html',result=res, content_type='application/json')

#return isolation page
@app.route('/isolation')
def isolation():
    sql = "SELECT * FROM fsquare.articles WHERE category = 'isolation'"
    res = db_query(sql)
    return render_template('isolation.html',result=res, content_type='application/json')


#returns mask page
@app.route('/mask')
def mask():
    sql = "SELECT * FROM fsquare.articles WHERE category = 'mask'"
    res = db_query(sql)
    return render_template('mask.html',result=res, content_type='application/json')

#returns next article page
@app.route('/<category>next/<id>', methods=['GET'])
def next(category, id):
    sql = "SELECT * FROM fsquare.articles WHERE category = '"+category+"' AND id > " + str(id)
    res = db_query(sql)
    # for the only one special article
    if (str(res[0]['id'])=='26' and res[0]['category']=='vaccine'):
        sql = "SELECT * FROM fsquare.articles WHERE category = 'vaccine' AND id = " + '26'
        res = db_query(sql)
        res=res[0]
        return render_template('blog-details-26.html', result=res, content_type='application/js')

    #if this is the last blog of this kind
    if(len(res)==1):
        res = res[0]
        #print('this is the last one')
        if (res['videoUrl'])!=None:
            return render_template('blog-details-with-video-last.html',result=res, content_type='application/json')
        else:
            return render_template('blog-details-last.html',result=res, content_type='application/json')
    #if having more than one next, just return the first one of them
    if(len(res)!=1):
        res = res[0]
    #check if there is video in this blog
    if (res['videoUrl'])!=None:
        return render_template('blog-details-with-video.html',result=res, content_type='application/json')
    else:
        return render_template('blog-details.html',result=res, content_type='application/json')



#returns previous article page
@app.route('/<category>previous/<id>', methods=['GET'])
def previous( category,id):
    sql = "SELECT * FROM fsquare.articles WHERE category = '"+category+"' AND id < " + str(id)
    res = db_query(sql)
    # for the only one special article
    if (str(res[-1]['id'])=='26' and res[0]['category']=='vaccine'):
        sql = "SELECT * FROM fsquare.articles WHERE category = 'vaccine' AND id = " + '26'
        res = db_query(sql)
        res=res[0]
        return render_template('blog-details-26.html', result=res, content_type='application/js')
    #if this is the first blog of this kind
    if(len(res)==1):
        res = res[0]

        if (res['videoUrl'])!=None:
            return render_template('blog-details-with-video-first.html',result=res, content_type='application/json')
        else:
            return render_template('blog-details-first.html',result=res, content_type='application/json')

    #if having more than one previous, just return the first one of them
    if(len(res)>1):
        res = res[-1]

    #check if there is video in this blog
    if (res['videoUrl'])!=None:
        return render_template('blog-details-with-video.html',result=res, content_type='application/json')
    else:
        return render_template('blog-details.html',result=res, content_type='application/json')

#vaccine page
@app.route('/vaccine')
def vaccine():
    return render_template('vaccine.html', content_type='application/json')

#vaccine map page
@app.route('/vaccine_map')
def vaccine_map():
    return render_template('vaccine-map.html', content_type='application/json')

#vaccine timeline page
@app.route('/vaccine_timeline')
def vaccine_timeline():
    return render_template('vaccine-timeline.html', content_type='application/json')

#vaccine blog page
@app.route('/vaccine_blog')
def vaccine_blog():
    sql = "SELECT * FROM fsquare.articles WHERE category = 'vaccine'"
    res = db_query(sql)
    return render_template('vaccine-blog.html',result=res, content_type='application/json')

#test page
@app.route('/test')
def test():
    return render_template('testing.html', content_type='application/json')

#test page
@app.route('/timeline')
def timeline():
    return render_template('timeline.html', content_type='application/json')

#test page
# @app.route('/26')
# def t():
#     sql = "SELECT * FROM fsquare.articles WHERE category = 'vaccine' AND id = " + '26'
#     res = db_query(sql)
#     res=res[0]
#     return render_template('blog-details-26.html', result=res, content_type='application/js')