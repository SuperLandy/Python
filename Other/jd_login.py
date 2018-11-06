#encoding:utf-8
from bs4 import BeautifulSoup
from urllib import request
import json,re
url = 'https://www.ithome.com/'
open = request.urlopen(url).read()
bet = BeautifulSoup(open,'lxml')
href1 = bet.find_all('a',attrs={'target':'_blank'})
for i in href1:
    print(i)
