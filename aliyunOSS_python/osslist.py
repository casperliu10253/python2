#!/usr/bin/env python
# -*- coding: utf-8 -*-

import oss2
import os
from getinfo import *

auth = oss2.Auth(accessKey_id, accessKey_secret) 
service = oss2.Service(auth, aliyun_url)

print(auth)
print(service)

for b in oss2.BucketIterator(service, prefix=bucketname):   #prefix 尋找指定字串
	print ("found: " + b.name)
	print ("-------------------------------------------")

f = open("/root/aliyunpython/tmp/osslist", "w")
print ("ALL osslist in this account: ")
print ("------------------------------------")
for c in oss2.BucketIterator(service):   #不指定字串 搜尋全部
        print (c.name)
        f.write(c.name + "\n")  

print ("------------------------------------")
f.close()


os.remove("lextab.py")
os.remove("getinfo.pyc")
os.remove("yacctab.py")
