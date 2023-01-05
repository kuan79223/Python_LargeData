
#### Python 的資料型態與 JSON 的資料型態略有差異:
![image](https://user-images.githubusercontent.com/112489587/200320067-b2cdb57a-207c-491e-8282-438b76b9a214.png)

#### 從 Python 到 JSON

1.以 json.dumps( ) 函數從 Python dictionary轉出JSON字串。    
2.以 json.dump( ) 函數從 Python dictionary轉出 JSON 檔案中。    
3.json資料於Python處理UTF8碼內容會產生亂碼，建議 dumps 時加入 
以下的參數才可以正確處理UTF8碼內容:ensure_ascii=False    
4.Python 與 JSON 檔案:   
  * JSON 檔案的中文資料於某些編輯軟體內會變成亂碼，但 Python 可以存取。   
  * 檔案寫入可用一般文件方式寫入，也可以使用 JSON 的方法寫入。    

### 先用 dumps.() 將字典轉成 json 字串格式    
![image](https://user-images.githubusercontent.com/112489587/200326324-72f84ad9-9754-425c-888c-e37a8cca7927.png)

### 再將 json 字串存成檔案使用 open() 方法   
![image](https://user-images.githubusercontent.com/112489587/200327146-1d8e5749-d084-4a3a-8f84-15791264fb4e.png)

### 將 dictionary 直接轉成 json 檔案   
![image](https://user-images.githubusercontent.com/112489587/200327235-e01fe70a-0eb8-4ae6-8426-6a302e0e1d34.png)

#### 創建一個空的字典裡面有一個 key 為 'people'   
[image](https://user-images.githubusercontent.com/112489587/200328374-76cb6cc4-2030-4993-a47d-40f2e4876fd9.png)

#### 使用 dump 寫入 json 檔案,必需使用 python 的 dictionary 物件    
![image](https://user-images.githubusercontent.com/112489587/200329768-9b752095-2137-45d9-8853-361c056fcbf8.png)

#### 使用 write 寫入時需使用的 json字串 格式   
![image](https://user-images.githubusercontent.com/112489587/200330077-a6e12b13-b704-46f5-b85b-308e27ca06e9.png)


#### 從 JSON 到 Python  
    以 json.loads( ) 函數從 JSON 字串中取出資料轉入 Python。
    以 json.load( ) 函數從 JSON 檔案中取出資料轉入 Python。
![image](https://user-images.githubusercontent.com/112489587/200341070-25c8e125-172f-4192-9eb8-92ea8e4f1336.png)



