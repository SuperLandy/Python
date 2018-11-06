# -*- coding: utf-8 -*-

from email.parser import Parser
from poplib import POP3_SSL
from email.header import decode_header
from email.utils import parseaddr


# 编码处理
def guess_charset(msg):
    charset = msg.get_charset()  # 从msg对象获取编码
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()  # 如果获取不到，再从content—type字段获取
        if 'charset' in content_type:
            charset = content_type.split('charset=')[1].strip()
            return charset
    return charset


# 数据解码
def decode_str(s):
    value, charset = decode_header(s)[0]  # 数据,数据编码方式，from email.header import decode_header
    if charset:
        value = value.decode(charset)
    return value


# print_ingo函数：
def print_info(msg, indent=0):  # indent用于缩进显示
    if indent == 0:
        for header in ['From', 'To', 'Subject']:  # 邮件的from、to、subject存在于根对象上
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)  # 需要解码subject字符串
                else:
                    # 解码mail地址
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = '%s' % (addr)
            print ('%s:%s' % (header, value))
            print('--' * 20)
    if (msg.is_multipart()):

        parts = msg.get_payload()  # 循环获得列表项
        for n, part in enumerate(parts):

            print_info(part, indent + 1)
    else:

        content_type = msg.get_content_type()  # 数据类型
        if content_type == 'text/plain' or content_type == 'text/html':  # 纯文本 html文本
            # 纯文本或html内容
            content = msg.get_payload(decode=True)  # 获得文本对象的字符串而非对象本身
            charset = guess_charset(msg)
            if charset: content = content.decode(charset)
            content = '%s' % (content)
            print (content)
        else:
            print('不是文本')


# 身份认证
user = '894562039@qq.com'
password = 'tkttjtcaiiumbcjf'
pop3_server = 'pop.qq.com'
server = POP3_SSL(pop3_server)
server.user(user=user)
server.pass_(password)
server.stat()
line = server.list()
new = len(line)
status, content, size = server.retr(1) #查找最新文件，status是状态， content是邮件内容，size是邮件大小

msg_content= b'\r\n'.join(content).decode('utf-8')
msg = Parser().parsestr(msg_content)

# 打印邮件内容，调用print_info函数:
print_info(msg)



# 关闭连接:
server.quit()