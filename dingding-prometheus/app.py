import os
import time
import json
import requests
import arrow
import hashlib
import hmac
import urllib
import base64
import pprint

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def send():
    if request.method == 'POST':
        post_data = request.get_data()
        send_alert(bytes2json(post_data))
        return 'success'
    else:
        return 'weclome to wqsp use prometheus alertmanager dingtalk webhook server!'


def bytes2json(data_bytes):
    data = data_bytes.decode('utf8').replace("'", '"')
    return json.loads(data)


def send_alert(data):
    pprint.pprint(data)
    token = os.getenv('ROBOT_TOKEN')
    secret = os.getenv('ROBOT_SECRET')
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    url = 'https://oapi.dingtalk.com/robot/send?access_token=%s&timestamp=%s&sign=%s' % (token, timestamp, sign)
    for output in data['alerts'][:]:
        try:
            pod_name = output['labels']['pod']
        except KeyError:
            try:
                pod_name = output['labels']['pod_name']
            except KeyError:
                pod_name = 'null'
                
        try:
            namespace = output['labels']['namespace']
        except KeyError:
            namespace = 'null'

        try:
            message = output['annotations']['message']
        except KeyError:
            try:
                message = output['annotations']['description']
            except KeyError:
                message = 'null'

        send_data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "prometheus_alert",
                "text": "**告警程序**:   k8s_alert \n" +
                        "**告警级别**:   %s \n\n" % output['labels']['severity'] +
                        "**告警类型**:   %s \n\n" % output['labels']['alertname'] +
                        "**故障pod**:   %s \n\n" % pod_name +
                        "**故障namespace**:   %s \n\n" % namespace +
                        "**告警详情**:   %s \n\n" % message +
                        "**告警状态**:   %s \n\n" % output['status'] +
                        "**触发时间**:   %s \n\n" % arrow.get(output['startsAt']).to('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss ZZ') +
                        "**触发结束时间**:   %s \n" % arrow.get(output['endsAt']).to('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss ZZ') +
                        "![screenshot](http://www.wq-sp.com/xpic/running_mode_detail_1.png)"
            }
        }
        req = requests.post(url, json=send_data)
        result = req.json()
        if result['errcode'] != 0:
            print('notify dingtalk error: %s' % result['errcode'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
