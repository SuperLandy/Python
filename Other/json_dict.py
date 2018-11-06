# encoding:utf-8
import json


data = '''
{
    "changed": true, 
    "rc": 0, 
    "stderr": "Shared connection to 47.100.95.135 closed.\r\n", 
    "stderr_lines": [
        "Shared connection to 47.100.95.135 closed."
    ], 
    "stdout": "负载情况: 0.09, 0.14, 0.06\r\ncpu使用率：8\r\n进程数：164\r\n内存使用情况：26.0251\r\n磁盘使用情况：10-1-8-75-\r\n磁盘文件数使用情况：5-1-13-2-\r\n", 
    "stdout_lines": [
        "0.09", 
        "8", 
        "164", 
        "26.0251", 
        "10-1-8-75-", 
        "5-1-13-2-"
    ]
}
'''  # ansible输出结果


newdata = json.loads(data, strict=False)  # 转换的时候使用strict跳过换行符


ip_info = newdata['stderr_lines']
ip_add = ip_info[0][21:-8]


std = newdata['stdout_lines']

inf = ''

cmd = '''
insert into server_for_2018_11(ip,cpu,task,menory,disk)values(
'%s','%s'
)''' % (str(ip_add), inf.join(std[1:-1]))

print(cmd)
