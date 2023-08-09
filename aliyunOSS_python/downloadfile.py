#!/usr/bin/env python
# -*- coding: utf-8 -*-

import oss2
import os
from getinfo import *
from os import walk
from os.path import join

auth = oss2.Auth(accessKey_id, accessKey_secret)        #取得 getinfo 裡的 accessKey_id, accessKey_secret 放入 auth
                                                        
bucket = oss2.Bucket(auth, aliyun_url, bucketname)      #取得 getinfo 裡的 aliyun_url, bucketname 加入 auth 放入 bucket

downpath = "/root/aliyunpython/download/"               #指定本地端下載的檔案目錄
f = open("filelist", "w")                               
for obj in oss2.ObjectIterator(bucket):
    print(obj.key)
    bucket.get_object_to_file(obj.key, downpath + obj.key)   #使用阿里雲參數 bucket.get_object_to_file (bucket上的檔案, 目錄/本地檔案名稱)下載檔案
    f.write(obj.key+"\n")

f.close()

os.remove("lextab.py")                      #os.remove 移除在執行的過程中產生的暫存檔
os.remove("getinfo.pyc")
os.remove("yacctab.py")

