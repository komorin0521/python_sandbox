#!/usr/bin/env python3

import argparse
import datetime
from time import ctime
import sys

# please install module using pip 
# (sudo) pip install ntp lib
import ntplib

__author__ = "oomori"
__version__ = "1.3.0"

class MyNTPClient(object):
    def __init__(self, ntp_server_host):
        self.ntp_client = ntplib.NTPClient()
        self.ntp_server_host = ntp_server_host

    def get_nowtime(self, timeformat = '%Y/%m/%d %H:%M:%S'):
        try:
            res = self.ntp_client.request(self.ntp_server_host)
            nowtime = datetime.datetime.strptime(ctime(res.tx_time), "%a %b %d %H:%M:%S %Y")
            return nowtime.strftime(timeformat)
        except Exception as e:
            print("An error occured")
            print("The information of error is as following")
            print(type(e))
            print(e.args)
            print(e)
            sys.exit(1)

def importargs():
    parser = argparse.ArgumentParser("NTP Clinet Sample")

    parser.add_argument("-ntp-server-host", "-n", help="ntp server",required=True,  type=str)
    parser.add_argument("-timeformat", "-t", required=False, type=str, default = '%Y/%m/%d %H:%M:%S' )
    args = parser.parse_args()

    return args.ntp_server_host, args.timeformat

def main():
    ntp_server_host, timeformat = importargs()
    ntp_client = MyNTPClient(ntp_server_host)
    print(ntp_client.get_nowtime(timeformat))

if __name__ == "__main__":
    main()
