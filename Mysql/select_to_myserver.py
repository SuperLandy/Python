#encoding:utf-8
import pymysql

def get_mysql(select):
    try:
        db = pymysql.connect(host='192.168.91.19',user='root',passwd='root',db='my_server')
        cursor =  db.cursor()
        cursor.execute(select)
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(e)
        pass
