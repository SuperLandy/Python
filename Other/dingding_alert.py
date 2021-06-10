import time
import hmac
import hashlib
import base64
import requests
import urllib.parse
import logging
import sys
from logging import handlers


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename, level='info', when='D', backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)
        self.logger.setLevel(self.level_relations.get(level))
        sh = logging.StreamHandler()
        sh.setFormatter(format_str)
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount, encoding='utf-8')
        th.setFormatter(format_str)
        self.logger.addHandler(sh)
        self.logger.addHandler(th)


def send_alert(webhook, secret, title, messages):
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    alert_url = webhook + '&timestamp=%s&sign=%s' % (timestamp, sign)
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": "### 告警主题: " + title + " \n >  " + messages + " \n >"
                    "![screenshot](http://www.wq-sp.com/xpic/running_mode_detail_1.png) \n"
        },
    }
    result = requests.post(alert_url, json=data)
    log.logger.info(result.json())


if __name__ == '__main__':
    log_path = '/var/log/dingding.log'  # log path
    alert_title = sys.argv[1]
    alert_messages = sys.argv[2]
    dingding_webhook = 'https://oapi.dingtalk.com/robot/send?access_token=' + '<your token>'
    dingding_secret = '<your_secret>'
    log = Logger(log_path, level='debug')
    send_alert(dingding_webhook, dingding_secret, alert_title, alert_messages)

