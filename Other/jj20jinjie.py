from urllib import request
from bs4 import BeautifulSoup
import time,http.cookiejar,urllib
img_link = []
file = open('sun_url.txt','r')
for link in file.readlines():
    img_link.append(link)
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'Accept-Ranges': 'bytes',
'ETag':'e839f5f96fcd31:0',
'Server': 'Microsoft-IIS/8.5'
}

x = 1

for src in img_link:

    try:
        last1_req = request.Request(url=src, headers=header)
        requs = request.urlopen(last1_req).read()
        # for k,v in req.getheaders():
        #     print(k,v,'\n')

        last_img_bf = BeautifulSoup(requs,features='lxml')
        last_img_link = last_img_bf.find_all('img', attrs={'id': "bigImg"})
        for ast in last_img_link:
            img_last_last = ast['src']
            filename = ast['alt']+'%s.jpg'%x
            print('正在下载第%s张图片...' % x)
            time.sleep(1)
            print(img_last_last)
            request.urlretrieve(url=img_last_last, filename='C:\\Users\zzq\PycharmProjects\py\sunjiajia\jj20\\%s' % filename)
            x = x+1
    except Exception:
        pass
