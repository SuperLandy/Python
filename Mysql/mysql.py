import pymysql
import os
import time
import json
db = pymysql.connect('192.168.91.19', 'root', 'root', 'xuexi')
cur = db.cursor()



def add():
    # 增加数据
    updat_sql = '''
    insert into tx(Host,user,password,cmd) values ('218.85.157.99','fjdx','fjdx','ping www.runoob.com')
    '''
    cur.execute(updat_sql)
    db.commit()


def search():
    # 查询数据
    cur.execute('select * from tx')
    data = cur.fetchall()
    return data


def delete():
    # 删除数据
    cur.execute('delete from tx where host="218.85.157.99"')
    db.commit()


def update():
    # 更新数据
    cur.execute('update tx set host = "14.215.177.38" where user = "root"')
    db.commit()


if __name__ == '__main__':
    print('welecome to mysql')
    print(' 1. 增加数据\n 2. 查询数据\n 3. 删除数据\n 4. 更新数据\n')
    use_chose = int(input('请选择你的操作类型：'))
    try:
        if use_chose == 1:
            add()
            print('数据增加成功\n')
        if use_chose == 2:
            db_data = list(search())
            print('查询成功, 查询结果如下：\n')
            for i in db_data:
                print(str(i))
        if use_chose == 3:
            delete()
            print('数据删除成功\n')
        if use_chose == 4:
            update()
            print('数据更新成功\n')
    except use_chose == 0:
        db.close()
        exit('程序正在退出..')
    except:
        print('输入有误！')
