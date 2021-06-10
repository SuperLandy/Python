#!/usr/bin/env python
# encoding: utf-8
import os
import sys
import pymysql


class SourceMysql(object):
    def __init__(self, mysql_host, mysq_user, mysql_passwd, mysql_port, exclude_list,  mysqldump_path, mysqldb_path):
        self.host = mysql_host
        self.user = mysq_user
        self.passwd = mysql_passwd
        self.port = mysql_port
        self.exclude_list = exclude_list
        self.mysqldump_path = mysqldump_path
        self.mysqldb_path = mysqldb_path
        self.total_dbname = []

    def source_select(self, sql):
        try:
            conn = pymysql.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd,
                port=self.port,
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
            )
            cur = conn.cursor()
            cur.execute(sql)
            res = cur.fetchall()
            cur.close()
            conn.close()
            return res
        except Exception as e:
            print(e)
            return False

    def get_all_db(self):
        sql = "show databases"
        result = self.source_select(sql)
        if not result:
            return False
        for i in result:
            db_name = i['Database']
            if db_name not in self.exclude_list:
                self.total_dbname.append(db_name)
        if not self.total_dbname:
            return False
        return self.total_dbname

    def dump_all_db(self):
        if not os.path.exists(self.mysqldump_path):
            sys.exit('mysqldump not found')
#         test_db_list = ['dbname1', 'dbname2', 'dbname3', 'dbname4', 'dbname5']  #测试数据
#         for db in test_db_list:

        for db in self.total_dbname:
            print('正在从%s导出数据库: ' % self.host, db)
            cmd = '''{mysqldump_path}  -h {host} -P {port} -u {user} -p{passwd} --single-transaction --default-character-set=utf8 --set-gtid-purged=OFF --databases {dbbame} > {dump_path}'''.format(
                mysqldump_path=self.mysqldump_path, host=self.host, port=self.port, user=self.user, passwd=self.passwd,
                dbbame=db,
                dump_path=self.mysqldb_path + '\\' + str(db) + '.sql')
            os.system(cmd)


class TargetMysql(object):
    def __init__(self, mysql_host, mysq_user, mysql_passwd, mysql_port, total_dbname, mysqlcmd_path, mysqldb_path):
        self.host = mysql_host
        self.user = mysq_user
        self.passwd = mysql_passwd
        self.port = mysql_port
        self.total_dbname = total_dbname
        self.mysqlcmd_path = mysqlcmd_path
        self.mysqldb_path = mysqldb_path

    def target_run(self, sql):
        try:
            conn = pymysql.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd,
                port=self.port,
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
            )
            cur = conn.cursor()
            cur.execute(sql)
            res = cur.fetchall()
            cur.close()
            conn.close()
            return res
        except Exception as e:
            print(e)
            return False

    def restore_db(self):

        if not os.path.exists(self.mysqlcmd_path):
            sys.exit('mysql command not found')

#         test_db_list = ['dbname1', 'dbname2', 'dbname3', 'dbname4', 'dbname5']  #测试数据
#         for db in test_db_list:
        for db in self.total_dbname:
            mysql_dump_file = self.mysqldb_path + '\\' + str(db) + '.sql'
            if not os.path.exists(mysql_dump_file):
                sys.exit('mysql dump file not found, file: %s' % mysql_dump_file)

            print('正在导入数据库: ', self.mysqldb_path + '\\' + str(db) + '.sql')
            cmd = '''{mysqlcmd_path}  -h {host} -P {port} -u {user} -p{passwd}  < {dump_path}'''.format(
                mysqlcmd_path=self.mysqlcmd_path, host=self.host, port=self.port, user=self.user, passwd=self.passwd,
                dump_path=mysql_dump_file)
            os.system(cmd)


if __name__ == '__main__':
    print("基于mysqldump 实现mysql到mysql 全量数据迁移, 实际使用需注意mysqldump与 mysqlserver版本情况")

    source_host = "10.1.1.10"                                       #源数据库地址
    source_user = "root"                                            #源数据库账号( 需要所有库权限 )
    source_passwd = "admin"                                         #源数据库密码
    source_port = 3306                                              #源数据库端口
    exclude_list = ["sys", "information_schema", "mysql", "performance_schema", "mysql_innodb_cluster_metadata"]
                                                                    #需要排除的数据库名称

    target_host = "10.1.2.10"                                       #目标数据库地址
    target_user = "root"                                            #目标数据库账号( 需要所有库权限 )
    target_passwd = "admin"                                         #目标数据库密码（特俗字符注意转义）
    target_port = 3306                                              #目标数据端口

    mysqldump_path = '/usr/bin/mysqldump'                           # mysqldump 绝对路径
    mysqlcmd_path = '/usr/bin/mysql'                                # mysqldump 绝对路径
    mysqldb_path = "/data/mysql_temp"                               # mysql导出绝对目录

    source_obj = SourceMysql(source_host, source_user, source_passwd, source_port, exclude_list, mysqldump_path, mysqldb_path)
    all_db_list = source_obj.get_all_db()  # 获取所有库名
    source_obj.dump_all_db()  # 导出所有库

    target_obj = TargetMysql(target_host, target_user, target_passwd, target_port, all_db_list, mysqlcmd_path,
                             mysqldb_path)
    target_obj.restore_db()
