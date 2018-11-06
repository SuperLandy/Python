#!usr/bin/env python
import os
ha_status = os.popen('ps -C haproxy --no-header |wc -l').read()
new = ha_status.stlip
if ha_status == 255:
    print(0)
else:

    print(1)
print(ha_status)