#!/usr/bin/env python2

import threading
import time

__author__ = "oomori"
__version__ = "1.0.0"

def myfunc(test_arg, results):
    """
    This is a test function of multithreading
    :param test_arg
    :return: None
    """
    print("call target_func")
    print("thread name is %s" % threading.current_thread().name)
    print(test_arg)
    output = test_arg * 2
    print("output is %d" % output)
    results[threading.current_thread().name] = output

def main():
    """
    main
    :return: None
    """

    results = dict()
    for _  in range(0, 10):
        threadlist = list()
        for thread_num in range(0, 5):
            thread = threading.Thread(target=myfunc, args=([thread_num, results]), 
                    name="thread%d" % thread_num)
            threadlist.append(thread)

        for thread in threadlist:
            thread.start()

        for thread in threadlist:
            thread.join()

        print("=== show each thread results ===")
        for k in results:
            print(k, results[k])
        time.sleep(5)

if __name__ == "__main__":
    main()
