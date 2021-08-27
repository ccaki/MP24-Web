import pymysql

class Database:
    def __init__(self):
        host = ""
        user = ""
        password = ""
        db = ""
        port = 3306

        self.con = pymysql.connect(host=host, user=user, password=password, db=db,
        port = port, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()


    #testing connection
#     def connection(self):
#         self.cur.execute("SELECT * FROM users LIMIT 50")
#         result = self.cur.fetchall()
#
#         return result

    #get table
    def get_from_table(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
