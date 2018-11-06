from bs4 import BeautifulSoup
from urllib import request
import pymysql
import lxml,time
#encoding:utf-8
header1 = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
'Cache-Control': 'no-cache'
}
last_url=[]
find_url=[]
time1 = []
def imgurl():
    url_0 = 'http://www.jj20.com/bz/nxxz/'
    req = request.Request(url=url_0)
    seq_0 = request.urlopen(req).read()
    url = BeautifulSoup(seq_0,features='lxml')
    img_link = url.find_all('a',attrs={'target':'_blank'})
    for item in img_link[2:]:
        firest_url = 'http://www.jj20.com'+item['href']

        for num in range(0,14):
            end_url = firest_url[:-5] + '_%s'%num+'.html'
            last_url.append(end_url)
    return last_url
def bsurl():
    for ll in last_url:
        try:
            get_head = request.Request(ll)
            get_html = request.urlopen(get_head).read()
            soup = BeautifulSoup(get_html,'lxml')
            find = soup.find_all('img',attrs={'id':'bigImg'})
            for date in find:
                find_url.append(date)

        except Exception as e:
            pass

    return find_url
def downpig():
    x = 0
    for sr in find_url:
        print('正在下载%s图片'%sr['alt'])
        filename = '{}{}.jpg'.format(sr['alt'],x)
        path = 'C:\\Users\\zzq\\PycharmProjects\\py\\sunjiajia\\jj20\\%s'%filename
        request.urlretrieve(sr['src'],path)
        x = x+1
        time.sleep(0.1)
imgurl()
bsurl()
m = 1
db = pymysql.connect('192.168.91.19','root','root','xuexi')
cur =  db.cursor()
for a in find_url:
    title = a['alt']+str(m)

    url = a['src']
    updat_sql = '''
        insert into pic_url(title,url)values ('%s','%s')
        ''' %(title,url)
    cur.execute(updat_sql)
    db.commit()
    print('正在写入第%s条数据'%m)
    m = m + 1
db.close()
print('全部写入')
# if __name__ == '__main__':
#     start_time = time.time()
#     print('#################程序即将启动第一阶段###############\n')
#     imgurl()
#     # pool = threadpool.ThreadPool(20)
#     # p1 = threadpool.makeRequests(imgurl(),args_list=[])
#     # for a1 in p1:
#     #     pool.putRequest(a1)
#     # pool.wait()
#     print('警告，一阶段已熄火！\n\n')
#
#     print('#################程序即将启动第二阶段###############\n\n')
#     bsurl()
#     # p2 = threadpool.makeRequests(bsurl(),args_list=[])
#     # for a2 in p2:
#     #     pool.putRequest(a2)
#     # print(find_url)
#     # pool.wait()
#     print('警告，二阶段已熄火！\n\n')
#
#     print('#################程序即将启动第三阶段###############\n\n')
#     downpig()
#
#     # p3 = threadpool.makeRequests(downpig(),args_list=[])
#     # for a3 in p3:
#     #     pool.putRequest(a3)
#     # pool.wait()
#     stop_time = time.time()
#     time1 = stop_time - start_time
#     print('全部下载完毕,本次下载共花费%s时间'%time1)pr

