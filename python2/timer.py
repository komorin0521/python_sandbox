#!/usr/bin/env python2
# -*- coding:utf-8 -*-

import time

__author__ = "oomori"
__version__ = "1.0.0"

class Timer(object):
    def __init__(self):
        self._result = dict()
        self._start_time_dict = dict()

    def start(self, key):
        if key in self._start_time_dict:
            raise NameError('%s is already registered' % key)
        else:
            self._start_time_dict[key] = time.time()

    def stop(self, key):
        if key not in self._start_time_dict:
            raise NameError("%s is not registerd" % key)
        elif key in self._result:
            raise NameError("%s is already calculating" % key)
        else:
            self._result[key] = time.time() - self._start_time_dict[key]

    def get_result(self, key):
        if key not in self._result:
            raise NameError("%s is not registerd or finished" % key)
        else:
            return self._result[key]

    def get_all_result(self):
        return self._result

