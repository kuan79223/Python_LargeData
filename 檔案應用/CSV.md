## introduce
1.檔案基本操作    
2.CSV 與JSON 操作    
3.檔案例外處理    
4.檔案關閉動作    

* 在讀取或寫入文件之前，必須使用 Python 內建的 open( ) 函數開啟 文件。     
這個函數將建立一個文件物件，這個文件物件會與真實的文件做連結，   
可讓您透過文件物件對文件進行存取動作。   
* UTF8 編碼資料還請加入另一個參數才可避免亂碼 : encoding='utf-8'   
* file object = open(file_name [, access_mode])   
file_name : file_name 參數是一個字串資料，代表包含要連結的文件名稱。   
* access_mode : access_mode 確定文件必須打開的模式，包括讀取、寫 入、附加等等。    
稍後會列完整列表。這是可選參數，默認文件訪問模式為 讀取(r)。    
#### Table_list
![image](https://user-images.githubusercontent.com/112489587/200160800-0f98c1e7-d11d-4c4f-b77a-7f16769c8edd.png)

#### 使用print()寫入
![image](https://user-images.githubusercontent.com/112489587/200161476-e0e71da6-12f3-46c7-95a8-168f27e1be0f.png)

#### 使用檔案實體方法write()寫入檔案
![image](https://user-images.githubusercontent.com/112489587/200161544-d1a7f9b0-5175-4834-ae71-04be29cbd9f0.png)

#### 範例
![image](https://user-images.githubusercontent.com/112489587/200161639-0fade770-f9f2-4fad-9bd4-bbe30eb2e1f3.png)

 執行後會路徑資料夾內創建一個.txt 檔  
![image](https://user-images.githubusercontent.com/112489587/200161646-1c884699-0156-4e01-ae34-4d391b53e17b.png)

## 檔案讀取

* read([size]) 方法   
  1. read([size]) 方法從文件當前位置起讀取 size 個字元數量， 
     若無參數，則代表讀取至文件結束為止。  
  2. 中文、英數與換行都是一格。 

![image](https://user-images.githubusercontent.com/112489587/200162029-110bc5a7-2b81-4bdc-bde4-bf3b9e17db55.png)

* readline 方法
1. 這個方法每次讀出一行內容，所以讀取時占用緩衝區較小，比較適合大型文件讀取，讀取到沒有資料為止。
* 若不使用 readline 可用 with 敘述一行一行讀取資料，再使用 for 迴圈 逐一進行處理。
* len( ) 代表計算字串字數。
* readlines 方法:   
  這方法將讀取整個文件所有行，保存在一個 list 內。 
* 讀取文件後可搭配使用的方法   
1.strip() 去除字串首尾的空白。  
2.lstrip( ) 去除字串左邊的空白。  
3.rstrip( ) 去除字串右邊的空白。  
4.startswith(‘字元’): 第一個字元。  

![image](https://user-images.githubusercontent.com/112489587/200162874-a6bca190-57b8-4f84-953e-57d4737fc82b.png)

![image](https://user-images.githubusercontent.com/112489587/200162911-e272c5e8-823c-4b09-a497-44976b50dd62.png)

# 寫入 CSV 檔案   
* 必須加入 import csv   
* 利用 writer( ) 可寫入資料，寫入時注意    
  1.delimiter - 這是代表分隔符號    
  2.quotechar - 這是代表包住字串的符號   
* 使用 writerow( ) 方法進行特定的儲存格寫入   

![image](https://user-images.githubusercontent.com/112489587/200165542-1d9fbc01-a4a9-461a-bdb3-2b5a2e21524c.png)

  在資料夾產生一個CSV檔
![image](https://user-images.githubusercontent.com/112489587/200165574-0fb3b733-d320-40a5-99f3-22bfe735e467.png)

#### 範例 
![image](https://user-images.githubusercontent.com/112489587/200171258-8ac081bb-0485-4cdd-810c-704cecb36b2c.png)

![image](https://user-images.githubusercontent.com/112489587/200171279-66d35bdf-f20c-48a0-9e81-f17798fb0d2b.png)

# 讀取 CSV 檔案
  逗點分隔（Comma-Separated Values，簡稱 csv）是一種簡單的文字檔格式，以逗號分隔不同欄位的資料，很多軟體在儲存與交換表格資料時都支援這樣的格式。  

* CSV 格式是資料庫最常用的導入和導出格式。  
* 資料均沒有類型，一切都是字串。  
* 沒有字體或顏色與儲存格寬度高度的設置。  
* Python 語法必須加入 import csv。  
* 讀取儲存格資料:  
1.reader( ):依照每一列的編號 由0開始  
2.DictReader( )  
  * 以第一列的值為每一行的名稱，第一列不是資料
  * 也可以重新命名，但第一列必須是資料
  
![image](https://user-images.githubusercontent.com/112489587/200176227-73fb3b3d-2443-4428-b744-436d45a95aba.png)

out >> 
![image](https://user-images.githubusercontent.com/112489587/200176252-7733151c-d66e-408d-ad19-293c19ee3140.png)

製作一個搜尋 Table 成績的程式
![image](https://user-images.githubusercontent.com/112489587/200176328-9524a8d1-b78f-4e86-9f14-cc4a70a6eaba.png)

![image](https://user-images.githubusercontent.com/112489587/200176373-5b652dda-cc26-44ad-a858-7ca0fcb8ca29.png)

out >> ![image](https://user-images.githubusercontent.com/112489587/200176442-e69eaf57-fa78-42e6-a484-19f0de3595bf.png)

![image](https://user-images.githubusercontent.com/112489587/200176497-6d0d9372-7929-4c44-9ac8-ff6d0699b2c5.png)

#### 將資料轉為2維的list => [ [ ] , [ ] , [ ] ] 
![image](https://user-images.githubusercontent.com/112489587/200177957-3fe7cd21-4253-4bdd-bbb7-af19686d2ac4.png)

out >> ![image](https://user-images.githubusercontent.com/112489587/200178101-c7a7d0eb-e2b4-4438-abea-3abf5f6bb4c9.png)



