#encoding:utf-8

class MyDatabase:
    def __init__(self,host,user,pwd,dbname,cmd):
        self.host = host
        self.user = user
        self.cmd = cmd
        self.pwd = pwd
        self.dbname = dbname
        self.Connect()

    def Connect(self):
        try:
            import pymysql
            db = pymysql.connect(self.host,self.user,self.pwd,self.dbname)
            cur = db.cursor(cursor=pymysql.cursors.DictCursor)
            cur.execute(self.cmd)
            data = cur.fetchall()
            #return data
            print(data)
        except pymysql.Error as error:
            #return error
            print(error)


MyDatabase('127.0.0.1','root','root','mysql','select host,user from user')
