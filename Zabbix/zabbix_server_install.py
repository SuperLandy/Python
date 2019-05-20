#!/usr/bin/python
#encoding:utf-8
import os,socket
#安装pip插件
os.system('yum -y install epel-release')
os.system('yum -y --enablerepo=epel install python-pip')
os.system('pip install --upgrade pip')
#安装pymysql
os.system('pip install pymysql')
os.system('yum clean all')

try:
    import pymysql
except Exception as err:
    print err

# 关闭selinux
Close_selinux = 'sed -i "s/SELINUX=enforcing/SELINUX=disabled/g" /etc/selinux/config'
Close_selinux_ls = 'setenforce 0'

#临时关闭防火墙
Close_firewall = 'systemctl stop firewalld'

#修改php的data州名
Modify_state = 'sed -i "s/Europe/Asia/g" /etc/httpd/conf.d/zabbix.conf'
#修改php的data地区名
Modify_region = 'sed -i "s/Riga/ShangHai/g" /etc/httpd/conf.d/zabbix.conf'
#取消php注释
Note_off = 'sed -i "s/# php_value/php_value/g" /etc/httpd/conf.d/zabbix.conf'


#安装rpm包
Install_rpm = 'rpm -Uvh https://repo.zabbix.com/zabbix/4.2/rhel/7/x86_64/zabbix-release-4.2-1.el7.noarch.rpm'

#安装zabbix依赖组件
Install_zabbix = 'yum install -y zabbix-server-mysql zabbix-web-mysql mariadb-server'

#初始化mysql密码,如修改需同时修改 DB_con 以及print密码
Initialization_passwd = 'mysqladmin -u root password root'

#解压导入zabbix数据库
Unzip = 'zcat /usr/share/doc/zabbix-server-mysql*/create.sql.gz | mysql -uzabbix -piamadmin zabbix'

#修改zabbix配置文件
Modify_zabbix = 'sed -i "s/# DBPassword=/DBPassword=iamadmin/g" /etc/zabbix/zabbix_server.conf'
Modify_zabbix_cache = 'sed -i "s/#CacheSize=8M/CacheSize=1024M/g" /etc/zabbix/zabbix_server.conf'



def install():
    '''安装zabbix-server'''
    # print('关闭相关服务...')
    os.system(Close_selinux)
    os.system(Close_selinux_ls)
    os.system(Close_firewall)

    # print('安装rpm包...')
    os.system(Install_rpm)

    # print('安装zabbix依赖组件...')
    os.system(Install_zabbix)

    # print('设置mysql...')
    os.system('systemctl start mariadb')
    os.system(Initialization_passwd)
    print 'mysql账号密码是：\n \033[1;31;40m root root \033[0m ''\n'
    print 'zabbix库账号密码是：\n \033[1;31;40m zabbix iamadmin \033[0m ''\n 请牢记此密码'
 

    # 连接mysql数据库
    DB_con = pymysql.connect('127.0.0.1', 'root', 'root', 'mysql')
    cursor = DB_con.cursor()
    cursor.execute('create database zabbix character set utf8 collate utf8_bin;')
    #设置zabbix库密码
    cursor.execute('grant all privileges on zabbix.* to zabbix@localhost identified by "iamadmin";')
    DB_con.commit()
    DB_con.close()

    # print('解压导入zabbix数据库')
    os.system(Unzip)

    # print('修改zabbix-server配置...')
    os.system(Modify_zabbix)
    os.system(Modify_zabbix_cache)

    # print('修改php配置...')
    os.system(Modify_state)
    os.system(Modify_region)
    os.system(Note_off)

    # print('正在启动相关服务')
    os.system('systemctl restart mariadb')
    os.system('systemctl start zabbix-server zabbix-agent httpd')
    os.system('systemctl enable zabbix-server zabbix-agent httpd')
def get_ip():
    '''获取本机通讯IP地址'''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('1.1.1.1', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    print '请使用浏览器打开 \033[1;31;40m http://%s/zabbix \033[0m 进一步配置zabbix web'%ip
if __name__ == '__main__':
    try:
        install()
    except Exception as err:
        print err
    get_ip()
