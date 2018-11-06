from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import request
import lxml,requests

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url='http://www.jj20.com/bz/nxxz/shxz/11077_5.html')
page = driver.page_source
soup = BeautifulSoup(page,features='lxml')
img_link = soup.find_all('img',attrs={'id':'bigImg'})

for i in img_link:
    filename = '%s.jpg'%i['alt']
    print(i['src'])

print('g')