from flask import Flask, render_template,current_app
from flask import request
#from dictionaries import Dict

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
# @app.route('/about')
# def about():
#     return render_template('about1.html')

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

#rumor page
@app.route('/rumor')
def rumor():
    return render_template('rumor.html', content_type='application/json')


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
@app.route('/test1')
def test1():
    return render_template('index-2.html', content_type='application/json')

#fact and fiction page
@app.route('/fiction')
def fiction():
    return render_template('factandfiction.html', content_type='application/json')


#visualisation page
@app.route('/visualisation')
def visualisation():
    return render_template('visualisation.html', content_type='application/json')

#test page
# @app.route('/26')
# def t():
#     sql = "SELECT * FROM fsquare.articles WHERE category = 'vaccine' AND id = " + '26'
#     res = db_query(sql)
#     res=res[0]
#     return render_template('blog-details-26.html', result=res, content_type='application/js')

#algorithm to search in a column in database
def search_in_db(keyword,res,col):
    sql = "SELECT *FROM  fsquare.articles WHERE `"+col+"` LIKE '%"+keyword+"%'"
    result = db_query(sql)
    for r in result:
        item = {}
        item['name'] = r['title']
        category = r['category']
        id = str(r['id'])
        item['link'] = '/'+category+'detail/'+id
        res.append(item)
    return res


#db title search algorithm
def title_search(keyword,res):
    res= search_in_db(keyword,res,'title')
    return res

#db content search algorithm
def content_search(keyword,res):
    res= search_in_db(keyword,body,'title')
    return res

#integrated database searching algorithm
def db_search(keyword,res):
    res = title_search(keyword, res)
    return res

#html names
htmls=['travel','transmission','hygiene','isolation','symptom','precaution','mask','fact','vaccine','fiction']
#html searching algorithm
def html_search(keyword,res):
    if keyword in htmls:
        name = "Read about "+keyword
        #for travel and hygiene, change the link names
        if (keyword =='travel'):
            keyword = 'travel_restriction'
        if (keyword =='hygiene'):
            keyword = 'good_hygiene'
        link = "/"+keyword
        item = {"name":name,"link":link}
        res.append(item)
    #print(res)
    return res




#integrated search algorithm
def search_algorithm(res, keyword):
    #format of res: a list of dic, key=title, value=href
    """
    e.g. [{"vaccine","/vaccine"},"vaccine_article","/articlelink"]
    """

    #search algorithm
    res = html_search(keyword,res)
    res = db_search(keyword,res)
    return res


#a dictionary for synonyms
synonym_dic={
    "travel":"travel",
    "travel ban":"travel",
    "travel restrictions":"travel",
    "travel bans":"travel",
    "masks":"mask",
    "respirator":"mask",
    "respirators":"mask",
    "quarantine":"isolation",
    "quarantines":"isolation",
    "self isolation":"isolation",
    "self-isolation":"isolation",
    "precautions":"precaution",
    "protection":"precaution",
    "protections":"precaution",
    "symptoms":"symptom",
    "transmissions":"transmission",
    "vaccines":"vaccine",
    "fact":"fiction",
    "facts":"fiction",
    "fictions":"fiction",
    "rumor":"fiction",
    "rumors":"fiction",
    "fact check":"fiction",
    "facts check":"fiction",
    "real":"fiction",
    "reality":"fiction",

    }
#find synonyms of keyword for better search results
def find_synonym(keyword):
    if keyword in synonym_dic.keys():
        keyword = synonym_dic[keyword]
    return keyword

#check if a keyword in sentence is meaningful
meaningless = ['what','where','when','how','the','and','who','a','an','but','however']
def is_meaningful(keyword):
    if keyword in meaningless:
        return False
    #include punctuation and single letters
    elif len(keyword)<3:
        return False
    else:
        return True

@app.errorhandler(404)
def page_not_found(e):
    # your processing here
    return render_template('error-404.html')

@app.route('/notfound', methods = ['POST', 'GET'])
def notfound():
    return render_template('error-404.html')

@app.route('/search/', methods = ['POST', 'GET'])
def search():
#     if request.method == 'GET':
#         return notfound()

    res = []
    if request.method == 'POST' or request.method == 'GET':
        form_data = request.form
        input = form_data['keyword']

        #make the input case insensitive
        input = input.lower()

        #find keyword in input
        if (' ' in input):
            keywords = input.split(' ')
            for keyword in keywords:
                #keyword grouping
                keyword = find_synonym(keyword)

                #only search if the keyword is meaningful
                if is_meaningful(keyword):
                    #get results
                    res = search_algorithm(res, keyword)

            #remove duplicate
            res1 = []
            for i in res:
                if i not in res1:
                    res1.append(i)
            res = res1

            #check if no search result is found
            if (len(res)>=1):
                return render_template('search.html',result = res)
            else:
                return render_template('noSearchResult.html')


        else:
            keyword = input
            #keyword grouping
            keyword = find_synonym(keyword)

            #get results
            res = search_algorithm(res, keyword)
            #print(res)

            #check if no search result is found
            if (len(res)>=1):
                return render_template('search.html',result = res)
            else:
                return render_template('noSearchResult.html')

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Error Message Text'
#         else:
#             return redirect(url_for('home'))
#     return render_template('index.html', error=error)