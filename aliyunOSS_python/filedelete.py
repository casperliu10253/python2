#!/usr/bin/env python
# -*- coding: utf-8 -*-

import oss2
import os
from getinfo import *

auth = oss2.Auth(accessKey_id, accessKey_secret)        #取得 getinfo 裡的 accessKey_id, accessKey_secret 放入 auth
                                                        
bucket = oss2.Bucket(auth, aliyun_url, bucketname)      #取得 getinfo 裡的 aliyun_url, bucketname 加入 auth 放入 bucket

prefix = raw_input("please insert prefix tag: ")

for obj in oss2.ObjectIterator(bucket, prefix=prefix):		#刪除某前綴的檔案
    bucket.delete_object(obj.key)
   
#### 列出 oss bucket 目前檔案列表 ####
f = open("filelist", "w") 
for obj in oss2.ObjectIterator(bucket):
    print(obj.key)
    f.write(obj.key+"\n")

f.close()



os.remove("lextab.py")                  #os.remove 移除在執行的過程中產生的暫存檔
os.remove("getinfo.pyc")
os.remove("yacctab.py")

