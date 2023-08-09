#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import oss2
from py3_getinfo import *
import requests
import os
import sys
import time

choose = input("(1)使用自有 app 域名 (2)自動產生 app 域名 :")
if choose == "1":
   counts = int(input("要輸入幾個域名: "))
   alldomain1 = []
   for i in range(counts):
       domain = input("appdomain(ex. abc.com): ")
       appdomain = ("https://" + domain)
       alldomain1 += [appdomain]    ### for迴圈執行結果依序放入 alldomain[]
       print("--------------------")
       print("appdomain%s: " % i+appdomain)
      
   restr = str(alldomain1)
   respace = restr.replace(" ","")  #把字串中空白刪除
   print(respace)
   realldomain = respace.replace("'","\"")   #把 ' 換成 \"
   str1 = '{"d":%s}' % realldomain   #把陣列輸出的字串帶入str1
   print("---------------------")
   ### json 格式用法 ###
   data = {
       "data": str1                #單行 json 格式 { "data": '{"d": ["https://%s","https://%s"]}' }
   }


elif choose == "2":
   #length = "6"
   maindomain = input("please insert the main domain(ex.abc.com): ")
   counts = int(input("要輸入幾個域名: "))
   #os.environ['length_shell']=length      ## 使用 os 模組 environ，定義一個 shell 變數，將python 的變數轉換成shell變數

   ## 自動產生 app doamin 放入陣列
   alldomain2 = []
   for i in range(counts):
        var = (os.popen("mkpasswd -l 6 -d 1 -c 1 -s 0 -C 0").read().strip()) #os.systen 的一種，需要加.read() 返回內容 
        ##for 迴圈內要用.strip()消除 \n
        print(var)
        appdomain = ("https://" + str(var) + brand + "." + maindomain) ## 要加入 str(var) 轉string
        alldomain2 += [appdomain]    ### for迴圈執行結果依序放入 alldomain[]
        print (appdomain)
	
        #print (alldomain)    ### 陣列輸出結果
        print("---------------------")
        ## 把陣列輸出結果單引號轉成雙引號
   restr = str(alldomain2)
   respace = restr.replace(" ","")  #把字串中空白刪除
   print(respace)
   realldomain = respace.replace("'","\"")   #把 ' 換成 \"
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


print(data)
### http post 加密 ###
url = 'https://domainhelper.mtchangeworld.com/api/v1/common/encrypt'
r =  requests.post(url, json=data)				#http post 
print(r)
print("Server responded:\n%s" % r.text)		#輸出 http post 結果,並用 strip() 參數過濾掉前後的 ""

encrypt = r.text.strip('"')			# 把輸出字串的 "" 移除
print("----------------------------")
print(encrypt)

### 寫入 q.png ###
mypath = "/root/aliyunpython/file/"
qpng = "q.png"
f = open(mypath + qpng,"w")
f.write(encrypt)
f.close()
print("file writed!")

### 確認寫入資料 ###
f = open(mypath + qpng)
text = f.read()
### http post 解密 ###

data2 = {
        "data" : text
}
print("data2:", data2)

print("----------- 解密 -----------")
url2 = 'https://domainhelper.mtchangeworld.com/api/v1/common/decrypt'
r2 = requests.post(url2, json=data2)
print(r2)
print("Server responded:\n%s" % r2.json())

f.close()


pronext = input("do you wanna continue?(y/n)")
if pronext == "y":
    print ("program well continue in 3s!")
    time.sleep(3)
    auth = oss2.Auth(accessKey_id, accessKey_secret)
    bucket = oss2.Bucket(auth, aliyun_url, bucketname)

    print("uploading files........")
    ### 目錄底下檔案上傳 ###

    for root, dirs, files in os.walk(mypath):         #python3 改成 os.walk
        for f in files:
            fullpath = (mypath + f)           #python3 join() 改成 變數.join()
            bucket.put_object_from_file(f, fullpath)  #bucket.put_object_from_file(oss檔名, 本機檔名)
            print("uploadfile = " + fullpath)

    print("upload completed!\n")
    time.sleep(1)
    ### 從 oss 下載檔案到 download 目錄 ###
    downpath = "/root/aliyunpython/download/"
    for obj in oss2.ObjectIterator(bucket):
        bucket.get_object_to_file(obj.key,downpath + obj.key)   #下載檔案到 download 目錄
        print("downloading files = "+ downpath + obj.key)

    print("download completed!\n")

else:
    print ("program stop!")
    sys.exit(1)             ## 輸入異常 結束程式(要 import sys)


downfile = "/root/aliyunpython/download/q.png"
print ("downfile: " + downfile)
f = open(downfile)
qpngtext = f.read()
### http post 解密 ###
data2 = {
	"data" : qpngtext
}
print("----------- 解密 -----------")
url2 = 'https://domainhelper.mtchangeworld.com/api/v1/common/decrypt'
r2 = requests.post(url2, json=data2)
print(r2)
print("Server responded:\n%s" % r2.json())

f.close()
