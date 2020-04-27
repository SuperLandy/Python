#-*- coding:utf-8 -*-
import os 
import argparse 
import socket
import struct
import select
import time
import smtplib
import sys
from email.mime.text import MIMEText
from email.header import Header


ICMP_ECHO_REQUEST = 8
DEFAULT_TIMEOUT = 1
DEFAULT_COUNT = 1 


class Email():
    def __init__(self,context):
        self.title = 'connet to host failed'  #邮件标题
        self.context = context              # 邮件正文
        self.sender = '456@qq.com'    # 发送邮件者名称
        self.receivers = ['123@qq.com'] #接收者邮箱  
        self.mail_host = "smtp.qq.com"     # 设置服务器
        self.mail_user = "123456@qq.com"    # QQ邮件登陆名称
        self.mail_pass = "123123123"     # qq邮箱生成的口令

    def post_email(self):
        '''
        :param title:邮件标题
        :param context: 邮件内容
        :return: 0:success, 1:failed
        '''
        message = MIMEText(self.context, 'plain', 'utf-8')
        message['From'] = Header(self.sender)  # 发送者
        message['To'] = Header(str(";".join(self.receivers)))  # 接收者
        message['Subject'] = Header(self.title)
        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            smtpObj.quit()

        except smtplib.SMTPException as error:
            print error

class Pinger(object):  
    def __init__(self, target_host, count=DEFAULT_COUNT, timeout=DEFAULT_TIMEOUT):
        self.target_host = target_host
        self.count = count
        self.timeout = timeout


    def do_checksum(self, source_string):
        """  ping包校验 """
        sum = 0
        max_count = (len(source_string)/2)*2
        count = 0
        while count < max_count:
            val = ord(source_string[count + 1])*256 + ord(source_string[count])
            sum = sum + val
            sum = sum & 0xffffffff 
            count = count + 2
     
        if max_count<len(source_string):
            sum = sum + ord(source_string[len(source_string) - 1])
            sum = sum & 0xffffffff 
     
        sum = (sum >> 16)  +  (sum & 0xffff)
        sum = sum + (sum >> 16)
        answer = ~sum
        answer = answer & 0xffff
        answer = answer >> 8 | (answer << 8 & 0xff00)
        return answer
 
    def receive_pong(self, sock, ID, timeout):
        """
        接收ping回包.
        """
        time_remaining = timeout
        while True:
            start_time = time.time()
            readable = select.select([sock], [], [], time_remaining)
            time_spent = (time.time() - start_time)
            if readable[0] == []: # Timeout
                return
     
            time_received = time.time()
            recv_packet, addr = sock.recvfrom(1024)
            icmp_header = recv_packet[20:28]
            type, code, checksum, packet_ID, sequence = struct.unpack(
                "bbHHh", icmp_header
            )
            if packet_ID == ID:
                bytes_In_double = struct.calcsize("d")
                time_sent = struct.unpack("d", recv_packet[28:28 + bytes_In_double])[0]
                return time_received - time_sent
     
            time_remaining = time_remaining - time_spent
            if time_remaining <= 0:
                return
     
     
    def send_ping(self, sock,  ID):
        """
        发送ping到指定host
        """
        target_addr  =  socket.gethostbyname(self.target_host)
     
        my_checksum = 0
     
        # Create a dummy heder with a 0 checksum.
        header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ID, 1)
        bytes_In_double = struct.calcsize("d")
        data = (192 - bytes_In_double) * "Q"
        data = struct.pack("d", time.time()) + data
     
        # Get the checksum on the data and the dummy header.
        my_checksum = self.do_checksum(header + data)
        header = struct.pack(
            "bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), ID, 1
        )
        packet = header + data
        sock.sendto(packet, (target_addr, 1))
     
     
    def ping_once(self):
        """
        Returns the delay (in seconds) or none on timeout.
        """
        icmp = socket.getprotobyname("icmp")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        except socket.error, (errno, msg):
            if errno == 1:
                # Not superuser, so operation not permitted
                msg +=  "ICMP messages can only be sent from root user processes"
                raise socket.error(msg)
        except Exception, e:
            print "Exception: %s" %(e)
    
        my_ID = os.getpid() & 0xFFFF
     
        self.send_ping(sock, my_ID)
        delay = self.receive_pong(sock, my_ID, self.timeout)
        sock.close()
        return delay
     
     
    def ping(self):
        """
        Run the ping process
        """
        for i in xrange(self.count):
            try:
                delay  =  self.ping_once()
            except socket.gaierror, e:   #ping错误
                failed_message = "Ping host failed, time: %s ,(socket error: '%s')" % (time.asctime( time.localtime(time.time())),e[1])
                send_email = Email(failed_message)
                send_email.post_email()
                print "Ping host failed. (socket error: '%s')" % e[1]
                break
     
            if delay  ==  None:  #ping超时
                timeout_message = "Ping host timeout, time: %s (timeout within %ssec.)" % (time.asctime( time.localtime(time.time())), self.timeout)
                send_email = Email(timeout_message)
                send_email.post_email()
                print "Ping host timeout. (timeout within %ssec.)" % self.timeout
            else:      #成功
                delay  =  delay * 1000
                print "Get pong in %0.4fms" % delay

if __name__ == '__main__':
    host = sys.argv[1]
    pinger = Pinger(target_host=host)
    while True:
        time.sleep(5)
        pinger.ping()
