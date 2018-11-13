#!/usr/bin/python  
import os
mysql_threads = os.system("mysqladmin -uroot -proot status | awk '{print$4}'")
#print mysql_threads
