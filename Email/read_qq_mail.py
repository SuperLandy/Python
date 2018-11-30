# -*- coding: utf-8 -*-

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


def guess_charset(msg):
    '''获取操蛋的编码'''
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def decode_str(s):
    '''获取到就开始解码'''
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def print_info(msg, indent=0):
    '''格式化输出邮件内容'''
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('Text: %s' % (content))
        else:
            print("有附件！！")


if __name__ == '__main__':
    '''邮箱认证信息'''
    user = '894562039@qq.com'
    password = 'tkttjtcaiiumbcjf'
    pop3_server = 'pop.qq.com'
    server = poplib.POP3_SSL(pop3_server)
    server.user(user)
    server.pass_(password)
    resp, mail, octets = server.list()
    mails = len(mail)
    resp, lines, octets = server.retr(mails - 0)  # -1是第二封邮件， -2第三封邮件
    msg_content = b'\n'.join(lines).decode('utf-8')
    msg = Parser().parsestr(msg_content)
    print_info(msg)
    server.quit()
