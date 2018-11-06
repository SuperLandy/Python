import urllib.request
import re
head = {
'Host': 'www.qiushibaike.com',
'If-None-Match': "2e006842cce98af7efc855cbb68325bf44bc8937",
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
url = 'https://www.qiushibaike.com/'

req = urllib.request.Request(url, headers=head)
res = urllib.request.urlopen(req)
patten = re.compile('<a.*?>\n<img.?>')
items = re.findall(patten)
for item in items:
    temp = item.replace('\n','')
    temp = temp.replace('</span></div>','')
    print(temp.replace(patten,'')+'\n')