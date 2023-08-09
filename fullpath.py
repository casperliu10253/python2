#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import walk
from os.path import join

# 指定要列出所有檔案的目錄
mypath = "/root/python/ziptest"
i = open("filepath.txt", "w")        ## 使用 w 覆寫

# 遞迴列出所有檔案的絕對路徑
for root, dirs, files in walk(mypath):
  for f in files:
    fullpath = join(root, f)
    i.write(fullpath + "\n")

i.close()            ## 縮排在最前面，會在for 迴圈執行完畢後關閉檔案

# 印出檔案內容
f = open("filepath.txt", "r")
words = f.read()
print(words)

f.close()
