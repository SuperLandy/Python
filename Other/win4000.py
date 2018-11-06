from bs4 import BeautifulSoup
from urllib.request import urlopen,urlretrieve
from urllib import request
import re,lxml
x = 0
all_link = []
header = {
'Connection': 'keep-alive',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'Host':'www.win4000.com'
}

try:
    for s in range(1,13):
        pig_url = 'http://www.win4000.com/wallpaper_detail_145655_%s.html'%s
        user_url = request.Request(url=pig_url,headers=header)
        html = urlopen(user_url).read()
        soup = BeautifulSoup(html,'lxml')
        img_class = soup.find_all('img',attrs={'class':'pic-large'})
        all_link.append(img_class)

    for s1 in range(1,10):
        pig_url_2 = 'http://www.win4000.com/wallpaper_detail_146322_%s.html'%s1
        user_ur2 = request.Request(url=pig_url_2, headers=header)
        html_1 = urlopen(user_ur2).read()
        soup_1 = BeautifulSoup(html_1,'lxml')
        img_class_1 = soup_1.find_all('img',attrs={'class':'pic-large'})
        all_link.append(img_class_1)

    for item in all_link:
        a = item[0]['src']
        urlretrieve(url=a,filename='C:\\Users\zzq\PycharmProjects\py\sunjiajia\win400\\%s.jpg'%x)
        print('正在下载第%s张图片'%x)
        x = x + 1

except Exception as e:
    print(e)
    pass

print('孙佳佳明确的告诉你，全部都下载成功啦')
