import requests
import json,time
from pprint import pprint

token = []
def get_token():
    del token[:]
    url = 'http://192.168.91.10/api/users/v1/token/'

    query_args = {
        "username": "admin",
        "password": "admin"
    }

    response = requests.post(url, data=query_args)

    token.append(json.loads(response.text)['Token'])

#get_token()

def get_user_info():

    url = 'http://192.168.91.10/api/terminal/v1/command/'

    for to in token:

        header_info = { "Authorization": 'Bearer ' + to }


        response = requests.get(url, headers=header_info)

        data = json.loads(response.text)
        if data == None:
            get_token()
            response_new = requests.get(url, headers=header_info)

            data_new = json.loads(response_new.text)
            return data_new
        else:
            response_new










#
# while True:
#     user_data = get_user_info()
#     for ab in user_data:
#         timestamp = ab['timestamp']
#         if timestamp > (int(time.time())-10) :
#             print('用户：'+ ab['user'],
#                   '资产：'+ ab['asset'],
#                   '输入：'+ ab['input'],
#                   # '输出：' + ab['output'],
#                   #'session:'+ ab['session']
#                   )
#
#             time.sleep(0.1)