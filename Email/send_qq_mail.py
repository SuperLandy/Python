#encode utf-8

import smtplib,getopt,sys
from email.mime.text import MIMEText
from email.header import Header

sender = '894562039@qq.com'  # 发送邮件名称
receivers = ['894562039@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
mail_host = "smtp.qq.com"  # 设置服务器
mail_port = 465  # 设置服务器
mail_user = "894562039@qq.com"  # QQ邮件登陆名称
mail_pass = "tkttjtcaiiumbcjf"  # qq邮箱生成的口令

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
if __name__ == '__main__':
    title = sys.argv[1]
    context=sys.argv[2]
    sed_mail = post_email(title,context)
    if sed_mail ==1:
        print('邮件发送success!')
    else:
        print('邮件发送失败')