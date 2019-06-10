#!/usr/bin/python36
#-*- coding:utf-8 -*-

import smtplib,sys
from email.mime.text import MIMEText
from email.header import Header

sender = '894562039@qq.com'  # 发送邮件名称
mail_host = "smtp.qq.com"  # 设置服务器
mail_port = 465  # 设置服务器
mail_user = "894562039@qq.com"  # QQ邮件登陆名称
mail_pass = "xtpjsapxfhkgbahh"  # qq邮箱生成的口令

def post_email(title, context):
    '''
    :param title:邮件标题
    :param context: 邮件内容
    :return: 0:success, 1:failed
    '''
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
    except smtplib.SMTPException as error:
        print(error)
        return 0
if __name__ == '__main__':
    receivers = sys.argv[1].split(',')
    title = sys.argv[1]
    context=sys.argv[2]
    sed_mail = post_email(title,context)
    # if sed_mail ==1:
    #     print('邮件发送success!')
    # else:
    #     print('邮件发送失败')