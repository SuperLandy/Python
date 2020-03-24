# !/usr/bin/env python3

def str_to_hex(x):
    for tt in x:
        print("".join(hex(ord(tt)).replace('0', '\\', 1)), end='')


text = "-1' select 1,2,3,4 ##"

abc = str_to_hex(text)
print(abc)
