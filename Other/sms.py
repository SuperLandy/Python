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
data = {"app_id":"153449D03D93B6EFD4EBB40DA10B9265","app_secret":"C5E1D12C447B966B56A4C39ECA633FF5",
        "app_signature":"486817DF1B35D765DA13E5CB1FFE6382",
        "bundle_id":"qq123","current_time":"1539066448033",
        "os_type":"i","request_id":"devVerifyId4485",
        "uid":""}
url = 'https://120.78.87.162/req/api/client/Developer/verify'
respon = requests.post(url,json=data,verify=False).json()
print(respon)
