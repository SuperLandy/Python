#!usr/bin/python
#encoding:utf-8
import matplotlib
from select_to_myserver import get_mysql
import matplotlib.pyplot as plt
cpu_info=[]
sq=[]
# 从mysql中取值，取不到跳过
for num in range(1,30):
    select="select menory from server_for_201808%02d where ip='120.78.86.254'"%num
    cpu = get_mysql(select)
    try:
        for b in cpu:
            cpu_info.append(float(b[0]))
    except:
        pass
for a in range(0,len(cpu_info)):
    sq.append(a)

# 添加x,y坐标标住
plt.xlabel('我宝佳天下第一',fontproperties='STSong')
plt.ylabel('内存',fontproperties='STSong')

#制图
plt.plot(sq,cpu_info)
plt.show()
