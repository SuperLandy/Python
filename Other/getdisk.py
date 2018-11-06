import psutil
usre_info = psutil.users()
cpu_info = psutil.cpu_count(logical=False)      #获取物理CPU总数
mem_info = psutil.virtual_memory()        #获取内存总数
disk_info = psutil.disk_usage('/')               #获取磁盘使用情况
net_info = psutil.net_io_counters()               #获取网络情况
print('''
当前登录用户是：%s,'\n'
当前CPU物理核数为：%s,'\n'
当前内存使用情况：%s,'\n'
当前网络情况为：%s
'''%(usre_info,cpu_info,mem_info,net_info))
