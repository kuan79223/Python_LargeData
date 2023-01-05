    import os
    import glob

#### 建立資料夾  在作業路徑下建立

    os.mkdir(os.path.join('folder'))


#### 在主目錄下建立檔案 os.mkdir(os.path.join( ' 資料夾名稱 ', ' 檔案名稱.副檔名 '))

    os.mkdir(os.path.join('folder','subfolder.txt'))
    os.mkdir(os.path.join('folder','subfolder.csv'))
    os.mkdir(os.path.join('folder','subfolder.xls'))
    os.mkdir(os.path.join('folder','subfloder.xml'))
    os.mkdir(os.path.join('folder','floder1.csv'))


### 利用 glob.glob 來讀取檔案路徑 讀出一個陣列型態

#### * 的意思就是匹配所有的內容

    All_content = glob.glob(os.path.join('folder','*'))


#### 可以自己設定要讀什麼檔案類型，像是：* txt  * csv

    csv_content = glob.glob(os.path.join('folder', '*csv'))
    
