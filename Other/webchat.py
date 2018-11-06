#conding:utf-8
import requests
import sys
import json
import re
file_path = 'access_token.log'    #本地access_token目录



Tlwtjcy = {
    #在此处输入员工信息
    "userid": "no3",                   #  新员工ID
    "name": "我是天才1",               # 新员工姓名
    "mobile": "13799009982",         # 新员工手机号
    "department": [1,2],               #新员工部门ID，可在通讯录中查看
    "position": "孙总",                #新员工职位
    "gender": "1",                      #新员工性别（1为男性，2为女性）
    "email": "894562239@qq.com",      #新员工邮箱
    "isleader": 1,                       #新员工是否为上级（1是上级，2是普通）
    "enable":1                           #是否启用该员工信息（1是启用，2是禁用）
}
def get_access_token():                     #向server获取access_token

    # corpid，管理端->我的企业
    corpid = 'ww50e3815f777ff526'
    # 在管理端->通讯录同步
    secrect = 'mqcYe4gW8oi02O5P5vF920CgsruknvFpT-fejXK-ISw'
#    grant_type = 'client_credential'
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s'%(corpid,secrect)
    r = requests.get(url)
    request_json = r.json()
    now_access_token = request_json['access_token']
    r.close()
    try:
        #请求成功时候，将access_token存入file_path文件中
        f = open(file_path,'w+')
        f.write(now_access_token)
        # print(now_access_token)
        f.close()
    except Exception as error:
        print(error)
def get_access_token_from_file():
    #读取本地access_token
   try:
        f = open(file_path,'r+')
        now_access_token = f.read()
        print('本次获取的access_token为：')
        f.close()
        return now_access_token
   except Exception as error:
        get_access_token()

if __name__ == '__main__':
         try:
             for i in range(0,1):
                access_token = get_access_token_from_file()
                useradd_url = ('https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=%s' % access_token)
                print(access_token)
                r = requests.post(useradd_url, data=json.dumps(Tlwtjcy))
                if re.search('42001',r.text):
                    print('access token 已过期')
                    get_access_token()
                    continue

                else:
                    print('更新成功')
         except Exception  as error:
             print(error)


