#encoding:utf-8
from __future__ import unicode_literals
from threading import Timer
from urllib import request
import wxpy,requests,json,time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import datetime
today = datetime.datetime.today().strftime('%m%d')
def get_info(date=''):
    url= 'http://open.iciba.com/dsapi/?date=%s'%today
    res = requests.get(url)
    note = res.json()['note']          #中文鸡汤
    content = res.json()['content']    #英文鸡汤
    #picture = res.json()['fenxiang_img']
    #filename = date + '.jpg'
    #request.urlretrieve(url=picture,filename=filename)
    return note,content



def send_info():
    bot = wxpy.Bot(console_qr=False, cache_path=True)
    try:
        mess=get_info()
        my_friend = bot.friends().search(u'Syun')[0]
        my_friend.send(mess[0])  # 发送中文鸡汤
        time.sleep(1)
        my_friend.send(mess[1])  # 发送英文鸡汤
        print('%s天的消息发送成功')
        # 每86400秒（1天），发送1次
        # t = Timer(30, send_info)
        # t.start()
    except wxpy.ResponseError as e:
        print('消息发送失败')
        print(e.err_code,e.err_msg)

if __name__ == '__main__':
    send_info()
    # a = 0
    # for a in range(1, 32):
    #     date = '201807%02d' % a
    #     #get_info(date=date)
    #     send_info(get_info(date=date))
    #     a = a + 1

