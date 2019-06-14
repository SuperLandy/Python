#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
import time
import json

from ansible.utils.path import makedirs_safe
from ansible.module_utils._text import to_bytes
from ansible.module_utils.common._collections_compat import MutableMapping
from ansible.parsing.ajson import AnsibleJSONEncoder
from ansible.plugins.callback import CallbackBase


class CallbackModule(CallbackBase):

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'log_plays'
    CALLBACK_NEEDS_WHITELIST = True


    def __init__(self):

        super(CallbackModule, self).__init__()

    def set_options(self, task_keys=None, var_options=None, direct=None):
        super(CallbackModule, self).set_options(task_keys=task_keys, var_options=var_options, direct=direct)

        self.log_folder = '/var/log/ansible/sunjiajia'

        if not os.path.exists(self.log_folder):
            makedirs_safe(self.log_folder)

    def log(self, host, category, data):
        if isinstance(data, MutableMapping):
            if '_ansible_verbose_override' in data:
                # 过滤不正常返回值
                data = 'omitted, data not allow'
                print(data)
            else:
                data = data.copy()
                print("host:%s"%str(host) +'\n' + data.get('stdout'))
    def runner_on_failed(self, host, res, ignore_errors=False):
        self.log(host, 'FAILED', res)

    def runner_on_ok(self, host, res):
        self.log(host, 'OK', res)

    def runner_on_skipped(self, host, item=None):
        self.log(host, 'SKIPPED', '...')

    def runner_on_unreachable(self, host, res):
        print('[ERROR]  host: {} is unracache, please check {} connection !!!\r\n'.format(host,host))
        #self.log(host, 'UNREACHABLE', res)

    def runner_on_async_failed(self, host, res, jid):
        self.log(host, 'ASYNC_FAILED', res)

    def playbook_on_import_for_host(self, host, imported_file):
        self.log(host, 'IMPORTED', imported_file)

    def playbook_on_not_import_for_host(self, host, missing_file):
        self.log(host, 'NOTIMPORTED', missing_file)
