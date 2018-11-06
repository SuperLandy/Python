import urllib
import http
import cookiejar
userpw= {
'userid':'qq_94214906t740',                #用户名密码
'pwd':'qq894562039'
}
date = urllib.parse.urlencode(userpw).encode()    #
cookie_filename = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
login_url = 'http://service.zol.com.cn/user/login.php'
user_agent= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
             'Connection': 'keep-alive'}
request = urllib.request.Request(url=login_url,data=date,headers=user_agent,method='post')
res = urllib.request.urlopen(request)
cookie.save(ignore_discard=True, ignore_expires=True)
print(cookie)

