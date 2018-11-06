#!/usr/bin/python3
#coding:utf-8
'''
这个脚本是为了我宝佳写的
'''

import requests,json,time,smtplib
from email.mime.text import MIMEText
from email.header import Header


url = 'http://192.168.91.17/zabbix/api_jsonrpc.php' #zabbix服务地址
sender = '894562039@qq.com'  # 发送邮件名称
receivers = ['340020779@qq.com','894562039@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
mail_host = "smtp.qq.com"  # 设置服务器
mail_port = 465  # 设置服务器
mail_user = "894562039@qq.com"  # QQ邮件登陆名称
mail_pass = "tkttjtcaiiumbcjf"  # qq邮箱生成的口令


# 封装一个方法直接传入邮件标题和内容
def post_email(title, context):
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(context, 'plain', 'utf-8')
    message['From'] = Header(sender)  # 发送者
    message['To'] = Header(str(";".join(receivers)))  # 接收者
    message['Subject'] = Header(title)
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        return 1
    except smtplib.SMTPException:
        return 0


def authenticate(url, username, password):
    # 配置zabbix登录验证获取token
    values = {'jsonrpc': '2.0',
              'method': 'user.login',
              'params': {
                  'user': username,
                  'password': password
              },
              'id': '1'
              }
    idvalue = requests.post(url,json=values)
    return idvalue.json()['result']

def alert_items(key,float_time):
    #获取所有告警信息
    values = {
    "jsonrpc": "2.0",
    "method": "alert.get",
    "params": {
        "output": "extend",
        "time_from": float_time},
    "auth": key,
    "id": 1}
    ale = requests.post(url,json=values)
    print(ale.json())
    return ale

def clear_data(data):
    # 对告警信息进行过滤筛选
    result = data.json()['result']
    for ab in result:
        ala = ab['message']
        info = ala[ala.index('alarmName') + 12:ala.index('entityName') - 3]
        return info



if __name__ == '__main__':
    #password = str(input('please input zabbix_password :' ))
    key = authenticate(url, 'Admin', 'zabbix')
    a = 0
    while True:

        float_time = time.time()
        data = alert_items(key,float_time)
        ab = clear_data(data=data)

        if ab != None:
            result = post_email("zabbix邮件告警通知",ab )
            print(ab)

        else:
            print("现在是第%s次"%a)
            a = a+1
            pass
        time.sleep(2)
