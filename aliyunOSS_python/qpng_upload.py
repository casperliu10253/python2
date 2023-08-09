#!/usr/bin/python
# -*- coding: utf-8 -*-

import oss2
import os
from getinfo import *
import requests
import readline
import json
import commands
from os import walk
from os.path import join
import random
import string
import time
import sys

choose = raw_input("(1)使用自有 app 域名 (2)自動產生 app 域名 :")
if choose == "1":
   counts = input("how many domain: ")
   alldomain1 = []
   for i in range(counts):
       domain = raw_input("appdomain(ex. abc.com): ")
       appdomain = ("https://" + domain)
       alldomain1 += [appdomain]    ### for迴圈執行結果依序放入 alldomain[]
       print("--------------------")
       print("appdomain%s: " % i+appdomain)
      
   restr = str(alldomain1)
   realldomain = restr.replace("'","\"")
   str1 = '{"d":%s}' % realldomain   #把陣列輸出的字串帶入str1
   print(str1)
   print("---------------------")
   ### json 格式用法 ###
   data = {
       "data": str1                #單行 json 格式 { "data": '{"d": ["https://%s","https://%s"]}' }
   }

elif choose == "2":
   length = 6
   maindomain = raw_input("please insert the main domain(ex.abc.com): ")
   counts = input("how many times do you want: ")
   os.environ['length_shell']=str(length)      ## 使用 os 模組 environ，定義一個 shell 變數，將python 的變數轉換成shell變數

   ## 自動產生 app doamin 放入陣列
   alldomain2 = []
   for i in range(counts):
	var = commands.getoutput('mkpasswd -l $length_shell -d 1 -c 1 -s 0 -C 0')
	appdomain = ("https://" + var + brand + "." + maindomain)
	alldomain2 += [appdomain]    ### for迴圈執行結果依序放入 alldomain[]
	print (appdomain)
	
	#print (alldomain)    ### 陣列輸出結果
	print("---------------------")
	## 把陣列輸出結果單引號轉成雙引號
   restr = str(alldomain2)
   realldomain = restr.replace("'","\"")

   str1 = '{"d":%s}' % realldomain   #把陣列輸出的字串帶入str1
   print(str1)
   print("---------------------")
   ### json 格式用法 ###
   data = {
      "data": str1		#單行 json 格式 { "data": '{"d": ["https://%s","https://%s"]}' }
   }
else: 
   print("Error: incorrect!!")
   sys.exit(1)			## 輸入異常 結束程式(要 import sys)

### http post 加密 ###
url = 'https://domainhelper.mtchangeworld.com/api/v1/common/encrypt'
r =  requests.post(url, json=data)				#http post  
print("Server responded:\n%s" % r.text.strip('"'))		#輸出 http post 結果,並用 strip() 參數過濾掉前後的 ""

f = open("/root/aliyunpython/file/q.png", "w")
f.write(r.text.strip('"'))

f.close()

try:
  pronext = raw_input("do you wanna continue?(y/n)")
  if pronext == "y":
	print ("program well continue in 3s!")
	time.sleep(3)
  else:
	print ("program stop!")
	sys.exit(1)		## 輸入異常 結束程式(要 import sys)
except:
  print("please insert y/n")
  sys.exit(1)			## 輸入異常 結束程式(要 import sys)

auth = oss2.Auth(accessKey_id, accessKey_secret) 
bucket = oss2.Bucket(auth, aliyun_url, bucketname)

print("uploading files........")
### 目錄底下檔案上傳 ###
mypath = "/root/aliyunpython/file/"

for root, dirs, files in walk(mypath):
  for f in files:
     fullpath = join(root, f)
     bucket.put_object_from_file(f, fullpath)  #bucket.put_object_from_file(oss檔名, 本機檔名)
     print("uploadfile = " + fullpath)

print("upload completed!\n")

### 從 oss 下載檔案到 download 目錄 ###
downpath = "/root/aliyunpython/download/"
for obj in oss2.ObjectIterator(bucket):
    #print(obj.key)
    bucket.get_object_to_file(obj.key,downpath + obj.key)   #下載檔案到 download 目錄
    print("downloading files = "+ downpath + obj.key)

print("download completed!\n")

#### 讀取下載後的檔案 ####
p = open("/root/aliyunpython/file/q.png", "r")
qpngfile = p.read()

p.close()

str2 = '"%s"' % (qpngfile)

print("decrypt string: \n" + str2.strip('"'))

data2 = {
    "data": str2
}

#### http post 解密 ####
url2 = 'https://domainhelper.mtchangeworld.com/api/v1/common/decrypt'

r = requests.post(url2, json=data2)			#http post
print("Server responded:\n %s" % r.text.strip('"')) 	#輸出 http post 結果,並用 strip() 參數過濾掉前後的 ""

os.remove("lextab.py")
os.remove("getinfo.pyc")
os.remove("yacctab.py")
