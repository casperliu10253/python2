需先產生 accountlist 檔案
accountlist 格式
[客戶]
bucketname = oss bucket 名稱
aliyun_url = oss endpoint
accessKey_id = OSS 權限的 key
accessKey_secret = OSS 權限的 key

需先安裝 pip install oss2 才能使用

getconf.py - 取得 accountlist 裡面的設定
osslist.py - 列出這個帳號內指定地區 例如.深圳 所有的 oss bucket
uploadfile.py - 上傳目錄底下所有檔案到指定的 bucket (目錄 files)
downloadfile.py - 取得 bucket 底下的檔案列表後下載到 download 目錄
bucketfiles.py - 列出這個 bucket 的檔案列表
qpng_upload.py - 輸入域名之後進行加密上傳，並從 oss 下載已上傳的資料進行解密確認

