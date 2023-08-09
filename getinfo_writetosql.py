#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import readline
import json
import requests
import pymysql
import logging

config = ConfigParser.ConfigParser()

config.read('allbrand')		#讀取 allbrand 文件

#print(config.sections())	#列出 accountlist 裡面所有的區塊[]標籤


def getmedia(brand):
## 用 requests.get url + header 驗證，並轉成 json 呈現 ##
	headers = {'apiKey':'123456'}                   #header 帶入 apikey  
	#brand = raw_input("please insert the brand name: ")
	url = config.get(brand,'url')
	print("brand= "+ brand)
	print("url= " + url) 
	print("---------------------------------------")
	global r         ## 區域變數
	r = requests.get(url, headers=headers)
	print json.dumps(r.json(), sort_keys=True, indent=4)

##### 處理r 取得的字串並列出 staticDomain 欄位 ######
	global rjson         ## 區域變數
	rjson = json.dumps(r.json(), sort_keys=True, indent=4)
	data = json.loads(rjson)
	global staticDomain
	staticDomain = data["staticDomain"]
	print ("media: " + data["staticDomain"])


def db_connect():            #資料庫連線
	try:
		sqldb = pymysql.connect(
			host = "127.0.0.1",
		    	user = "root",
		    	password = "123456",
		    	db = "media",
		    	charset = "utf8"
			)
		return sqldb                ## 傳回 sqldb 的資料庫連線資訊
	except Exception as e:
        	logging.error('Fail to connection mysql {}'.format(str(e)))
		return None

def create_tables():                #建立 資料庫 table (須先建立資料庫)
	try:
		if conn is not None:
		        cur = conn.cursor()
		        print ("connect successful")
		if cur is not None:                    # table 格式     #mediainfo 為資料表名稱  
        		sql = 'create table if not exists `mediainfo`( \                        
        		`id` int unsigned auto_increment, \
        		`brand` varchar(16) not null, \
        		`domain` varchar(255) not null, \
			`submission_date` date, \
			primary key (id) \
        		)engine=InnoDB default charset=utf8'
        		cur.execute(sql)
			print("table created")
#需開頭為 `id` int unsigned auto_increment  結尾為 primary key (id) \ 作為索引

        except Exception as e:
                logging.error('Fail to connection mysql {}'.format(str(e)))

def insert_info():            #把取得資料寫入資料庫
	try:
### pymysql 操作資料庫時需要啟動一個 conn.cursor 游標 ###
		cur = conn.cursor()                
	    	sql = 'INSERT INTO mediainfo (`brandid`, `media_domain`, `timestamp`) VALUES (%s, %s ,NOW())'
	    	cur.execute(sql, (brand, staticDomain))
	    	conn.commit()                # 提交
		print('insert into mediainfo successful')
	        
        except:
        # 發生錯誤就回滾
                print ("Failed rollback")
                conn.rollback()
        # 關閉cursor()方法
                cur.close()

        # 關閉資料庫連線
                conn.close()

def show_media():         #進入資料庫讀取資料
	cur = conn.cursor()
	sql = 'select * from mediainfo'
	cur.execute(sql)
	resultall = cur.fetchall()
	print (resultall)

def update_sql():            #更新資料表內容，用法為 update 資料表 set 關鍵字(多個關鍵字用逗點連接)     where 尋找指定欄位
        cur = conn.cursor()
        sql = 'UPDATE mediainfo SET domain=%s ,submission_date=NOW() WHERE brand=%s'
        cur.execute(sql, (domain,brand))
        conn.commit()
        print("sql "+brand+" updated")

brand = raw_input("please insert the brand name: ")
conn = db_connect()                ##使用 db_connect()  的函式 >> (跳到db_connect())
getmedia(brand)                        ##使用 getmedia(brand)  的函式 >> (跳到getmedia(brand)  )
#create_tables()

#### 選擇使用方法 ####
choose = raw_input("(1)create_tables (2)insert_info (3)show_media : ")
if (choose == "1"):
	create_tables()                    ## 使用 create_tables() 的函式 >> (跳到create_tables() )

elif (choose == "2"):
	insert_info()                           ##使用 insert_info() 的函式 >> (跳到 insert_info())

elif (choose == "3"):
	show_media()                        ##使用 show_media() 的函式 >> (跳到show_media() )
