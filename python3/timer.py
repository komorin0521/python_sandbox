#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Timer module
"""

import time

__author__ = "oomori"
__version__ = "1.0.0"


class Timer(object):
    """
    This is a timer class

    usage example:

    timer = Timer()
    timer.start("test")
    ...
    timer.stop("test")
    timer.get_result("test") #you can get the elapsed time

    timer.start("test2")
    ...
    timer.stop("test2")

    result = timer.get_all_result() # you can get all result as dictionary
    """

    def __init__(self):
        """
        init function
        """
        self._result = dict()
        self._start_time_dict = dict()

    def start(self, key):
        """
        Start calculating time of a key you request.
        If key is already registered, this function raises error
        :param key: The key of timer
        :return: None
        """
        if key in self._start_time_dict:
            raise NameError('%s is already registered' % key)
        else:
            self._start_time_dict[key] = time.time()

    def stop(self, key):
        """
        Stop calculating time of a key you request.
        If the key is not registered or already finish calculating,
        this function raises an error
        :param key: The key you want to start calculating
        :return: None
        """
        if key not in self._start_time_dict:
            raise NameError("%s is not registerd" % key)
        elif key in self._result:
            raise NameError("%s is already calculating" % key)
        else:
            self._result[key] = time.time() - self._start_time_dict[key]

    def get_result(self, key):
        """
        Getting a elapsed time of the key you requested.
        :param key: The key you want to get elapsed time
        :return: An eplapsed time of the key
        """
        if key not in self._result:
            raise NameError("%s is not registerd or finished" % key)
        else:
            return self._result[key]

    def get_all_result(self):
        """
        Getting all results you calculated elapsed time.
        :return: The all results you calculated elapsed time.
        """
        return self._result
