#!/usr/bin/env python3

from time import ctime
import datetime

# please install module using pip 
# (sudo) pip install ntp lib
import ntplib

__author__ = "oomori"
__version__ = "1.1.0"

class MyNTPClient(object):
    def __init__(self, ntp_server_host):
        self.ntp_client = ntplib.NTPClient()
        self.ntp_server_host = ntp_server_host

    def get_nowtime(self, timeformat = '%Y/%m/%d %H:%M:%S'):
        res = self.ntp_client.request(self.ntp_server_host)
        nowtime = datetime.datetime.strptime(ctime(res.tx_time), "%a %b %d %H:%M:%S %Y")
        return nowtime.strftime("%Y/%m/%d %H:%M:%S")

def main():
    ntp_client = MyNTPClient('ntp.nict.jp')
    print(ntp_client.get_nowtime())

if __name__ == "__main__":
    main()
