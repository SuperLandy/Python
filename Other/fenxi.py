import json
b=json.loads('''{ "changed": true,
    "rc": 0, 
    "stderr": "Shared connection to 47.100.95.135 closed.\r\n", 
    "stderr_lines": [
        "Shar ed connection to 47.100.95.135 closed."
    ], 
    "stdout": "负载情况: 0.01, 0.07, 0.03\r\ncpu使用率：8\r\n进程数：163\r\n内存使用情况：24.8307\r\n挂载点/dev/vda1使用率: 9%\r\n挂载点tmpfs使用率: 1%\r\n挂载点/dev/vdc1使用率: 8%\r\n挂载点/dev/vdb1使用率: 69%\r\n挂载点/dev/vda1文件数: 9%\r\n挂载点tmpfs文件数: 1%\r\n挂载点/dev/vdc1文件数: 8%\r\n挂载点/dev/vdb1文件数: 69%\r\n", 
    "stdout_lines": [
        "负载情况: 0.01, 0.07, 0.03", 
        "cpu使用率：8", 
        "进程数：163", 
        "内存使用情况：24.8307", 
        "挂载点/dev/vda1使用率: 9%", 
        "挂载点tmpfs使用率: 1%", 
        "挂载点/dev/vdc1使用率: 8%", 
        "挂载点/dev/vdb1使用率: 69%", 
        "挂载点/dev/vda1文件数: 9%", 
        "挂载点tmpfs文件数: 1%", 
        "挂载点/dev/vdc1文件数: 8%", 
        "挂载点/dev/vdb1文件数: 69%"
    ]}''')
print(b['changed'])