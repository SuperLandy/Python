#coding utf-8
import requests
import re
import json
import time
start_time = time.time()
from multiprocessing import Pool


headers = {'User-Agent','Mozilla/5.0'}
def download(url):                                   #定义html下载器
    try:
        res = requests.get(url,headers=headers)
        if res.status_code==200:
            return res.text
        return None
    except requests.RequestException:
        return None


def parse(html):                                   #定义html解释器
    pattern = re.compile(('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                        +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                        +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S))
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'soure':item[5]+item[6]

        }

def cunchu(content):                    #定义存储
    with open('result.txt','a',encoding='utf-8')as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def main(morenset):                   #初始化
    url = 'http://maoyan.com/board/4?offset='+str(morenset)
    html = download()
    for item in parse(html):
        print(item)
        cunchu(item)

if __name__ == '__main__':
   p = Pool()
   p.map(main,[i*10 for i in range(10)])