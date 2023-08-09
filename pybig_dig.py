#!/bin/python
# coding: utf-8
import readline
import dns.resolver
import os
digname = raw_input("please insert the domainlist(ex. abc.com cde.com) ")
#diglist = digname.split(' ', 2 )                 ## 以空白為間隔切割字串放入變數，後面那個 2 是兩個放一起 ex. ['123.com','456.com','123.com 456.com']，可不加
diglist = digname.split(' ')                 
print(diglist)

len1 = len(diglist)				 ## 計算 diglist 陣列的數量

''' dns resolver 指定dns server 方式
myResolver = dns.resolver.Resolver()
myResolver.nameservers = ['1.1.1.1']
myAnswers = myResolver.query("www.google.com", "A")
for rdata in myAnswers:
    print(rdata)
'''


#####################
fp = open("/root/bigdig/pyresult","a")			## 開啟文件並於執行時使用 print >> fp 寫入 /root/bigdig/pyresult
myResolver = dns.resolver.Resolver()			## 指定 myResolver = dns.resolver.Resolver() 函式庫
myResolver.nameservers = ['8.8.8.8']			## 指定 myResolver 使用的 dns server
for i in range(len1):
   print >> fp,("---------- " + diglist[i] + " ----------" )
   try:
	a = myResolver.query(diglist[i], 'A')		## 使用 myResolver.query 取得 domain A 紀錄
 	for j in a.response.answer:
		print>>fp,(j)
   except Exception:
	print >> fp,(diglist[i] + " no A record")	## 如果出現錯誤就顯示 no A record
   try:
        cname = myResolver.query(diglist[i], 'CNAME')	## 使用 myResolver.query 取得 domain CNAME 紀錄
        for h in cname.response.answer:
                print >> fp,(h)
   except Exception:
        print >> fp,(diglist[i] + " no CNAME record")	## 如果出現錯誤就顯示 no CNAME record
   try:
        ns = myResolver.query(diglist[i], 'NS')		## 使用 myResolver.query 取得 domain NS 紀錄
        for k in ns.response.answer:			
                print >> fp,(k)
   except Exception:
        print >> fp,(diglist[i] + " no NS record")	## 如果出現錯誤就顯示 no NS record

fp.close()

with open('/root/bigdig/pyresult', 'r') as f:		## 開啟 /root/bigdig/pyresult 並印出內容
    data = f.read()
    print(format(data))

os.remove("/root/bigdig/pyresult")
