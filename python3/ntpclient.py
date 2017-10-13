#!/usr/bin/env python3

from time import ctime
import datetime

# please install module using pip 
# (sudo) pip install ntp lib
import ntplib

__author__ = "oomori"
__version__ = "1.0.0"

ntp_client = ntplib.NTPClient()
res = ntp_client.request('ntp.nict.jp')
nowtime = datetime.datetime.strptime(ctime(res.tx_time), "%a %b %d %H:%M:%S %Y")

print(nowtime.strftime("%Y/%m/%d %H:%M:%S"))

