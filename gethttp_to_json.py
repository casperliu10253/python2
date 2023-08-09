#!/bin/python
#coding: utf-8
import requests
import json

####### 因為 python 2.7 是 unicode 編碼，所以輸出會有異常，加入這段 def class 轉編碼 #######
def unicode_convert(input):
    if isinstance(input, dict):
        return {unicode_convert(key): unicode_convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [unicode_convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
##########################################

r = requests.get("http://google.com")
str = r.text

jsonstr = unicode_convert(json.loads(str))

print (jsonstr)
print ("-----------------------------------")
print (jsonstr['serverDomains'])        ## python 2.7 預設為 unicode 所以輸出前面會變成 u''

print ("-----------------------------------")
