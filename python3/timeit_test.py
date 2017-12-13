#!/usr/bin/env python3

import time
import timeit

def test_func(inputs, sleep_time=5):
    """
    This is a test function
    :param inputs:
    :param sleep_time:
    :return:
    """
    print("call func of test_func")
    print("inputs = %d" % inputs)
    print("sleep_time = %d" % sleep_time)
    time.sleep(sleep_time)


def main():
    """
    main
    :return: None
    """
    inputs = 10
    results = timeit.repeat("test_func(inputs, sleep_time)", repeat=5, number=1, setup="from __main__ import test_func;inputs,sleep_time=%d, 2" % inputs)

    print(results)

if __name__ == "__main__":
    main()
