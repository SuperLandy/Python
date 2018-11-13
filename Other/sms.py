import requests,time,hashlib

from requests.packages.urllib3.exceptions import *
requests.packages.urllib3.disable_warnings()

#
#
# def getmd5(str):
#     '''MD5 加密'''
#     md5 = hashlib.md5()
#     md5.update(str.encode())
#     key = md5.hexdigest()
#     return key
#
# time=millis = int(round(time.time() * 1000))  #获取13位时间戳
# appid="FE1D963B5963386E85DC95C36C5BC5A4"
# si="41CC29F71904A14A79F8A83196C38E4B"
# a=si+str(time)
# sign=getmd5(a)
# data = {
#     "sign": sign,
#     "app_id": appid,
#     "sms_template": "一点登录",
#     "sms_param": {"code": "123456"},
#     "tel": "15060017668",
#     "time_stamp13":time
# }
#
# post=requests.post(url='https://120.78.87.162/req/api/server/Sms/smsSend',json=data,verify=False)
#
# print(post.json())
#
time = int(round(time.time() * 1000)) 

print(time)
data = {"app_id":"51DC2C9280655F29ACF5E0D66A4B6A10",
"app_token":"F692A75A61CD5CD8F2D4AED31CEF4F8B58CFDFAFAF042BC0D8E99BA873C21DBD",
"request_id":"saiVerify2498","tel":"14759157156",
"temp_code":"012707763621949D:391",
"uid":"1A2CB6FB838656290BFBE0B2564FC874","version":"1.1.1"}

url = 'http://120.78.87.162/req/api/client/Developer/verify'
respon = requests.post(url,json=data).json()
print(respon)
