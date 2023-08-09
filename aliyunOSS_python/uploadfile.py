#!/usr/bin/env python
# -*- coding: utf-8 -*-

import oss2
import os
from getinfo import *
from os import walk
from os.path import join

auth = oss2.Auth(accessKey_id, accessKey_secret)            #取得 getinfo 裡的 accessKey_id, accessKey_secret 放入 auth
                                                            
bucket = oss2.Bucket(auth, aliyun_url, bucketname)          #取得 getinfo 裡的 aliyun_url, bucketname 加入 auth 放入 bucket

#oss2.resumable_upload(bucket,"bucketfilename","localfilename") #單一上傳

### 指定本機目錄上傳全部檔案 ###
mypath = "/root/aliyunpython/file/"

for root, dirs, files in walk(mypath):
  for f in files:
     fullpath = join(root, f)
     bucket.put_object_from_file(f, fullpath)  #bucket.put_object_from_file(bucket檔名, 本機檔名)

os.remove("lextab.py")                          #os.remove 移除在執行的過程中產生的暫存檔
os.remove("getinfo.pyc")
os.remove("yacctab.py")

