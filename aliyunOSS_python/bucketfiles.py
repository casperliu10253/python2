#!/usr/bin/env python
# -*- coding: utf-8 -*-

import oss2
import os
from getinfo import *

auth = oss2.Auth(accessKey_id, accessKey_secret)        #取得 getinfo 裡的 accessKey_id, accessKey_secret 放入 auth

bucket = oss2.Bucket(auth, aliyun_url, bucketname)      #取得 getinfo 裡的 aliyun_url, bucketname 加入 auth 放入 bucket

f = open("filelist", "w")                               #產生寫入的檔案
for obj in oss2.ObjectIterator(bucket):                 #使用阿里雲的參數 oss2.ObjectIterator() 用for迴圈出來
    print(obj.key)                                      #obj.key 顯示出找到的結果
    f.write(obj.key+"\n")

f.close()

os.remove("lextab.py")                                  #os.remove 移除在執行的過程中產生的暫存檔
os.remove("getinfo.pyc")
os.remove("yacctab.py")



