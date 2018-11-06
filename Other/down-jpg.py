from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import re

url = 'http://www.netbian.com/'
html  = urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
im_link = soup.find_all('img',{'src':re.compile('.*?\.jpg')})[1:-1]
x = 0
for link in im_link:
    down_link = link['src']
    try:
        name = 'c:\\Users\zzq\PycharmProjects\py\sunjiajia\\netbian\%s.jpg'%x
        urlretrieve(down_link,filename=name)
        x = x+1
    except:
        pass
print("恭喜你下载成功")
