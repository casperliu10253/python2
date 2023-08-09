#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import readline

config = ConfigParser.ConfigParser()    #ConfigParser 傳遞參數

config.read('accountlist')		#讀取 config 

#print(config.sections())	#列出 accountlist 裡面所有的區塊[]標籤

brand = raw_input("please insert the brand name: ")

bucketname = config.get(brand,'bucketname')
aliyun_url = config.get(brand,'aliyun_url')
accessKey_id = config.get(brand, 'accessKey_id')
accessKey_secret = config.get(brand, 'accessKey_secret')

print("brand= "+ brand)
print("bucketname= " + bucketname) 
print("aliyun_url= " + aliyun_url)
print("accessKey_id= "+ accessKey_id)
print("accessKey_secret= " + accessKey_secret)

print("---------------------------------------")
