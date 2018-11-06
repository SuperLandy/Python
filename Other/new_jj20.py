#coding:utf-8
from urllib import request
from bs4  import BeautifulSoup
import lxml,requests,re,sys,os
header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
head = 'http://www.5857.com/pcbz/76035_'
x = 0




for num in range(2,13):
    link = head + str(num) + '.html'
    url = request.Request(url=link,headers=header)
    respon = request.urlopen(url).read()
    soup = BeautifulSoup(respon,'lxml')
    img_link = soup.find_all('img',{'src':re.compile('http://d.5857.com/kbh.*?\.jpg')})
    for i in img_link:
        filename = '%s%s.jpg'%(i['alt'],x)

        request.urlretrieve(i['src'],filename)

        print('正在下载%s'%i['alt'])
        x = x+1

print('game over')
