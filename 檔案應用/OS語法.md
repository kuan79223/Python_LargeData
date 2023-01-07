    import os

#### 傳回檔案完整的路徑名稱
    
    filename = os.path.abspath('main.py')
    
![image](https://user-images.githubusercontent.com/112489587/210712918-f944617d-609b-4c18-80cd-2e49039066be.png)

#### 檢查指定的檔案或路徑是否存在
    
    if os.path.exists(filename):
#### 最後的檔案或路徑名稱
    
    basename = os.path.basename(filename)

![image](https://user-images.githubusercontent.com/112489587/210713055-aaecd191-8a68-4ba1-a40b-e8a15c138de5.png)

    
#### 利用 os.path.basename(完整路徑).split('.')[0] ,或者 os.path.splittext 切除附檔名

    basename1 = os.path.basename(filename).split('.')[0]
    
    basename2 = os.path.splitext(os.path.basename(filename))[0]
    
    
out >> main
    
#### 回傳目前檔案目錄路徑    
   
    os.getcwd()
    
    os.path.dirname(filename)


* 兩個語法得到了相同的路徑  
    ![image](https://user-images.githubusercontent.com/112489587/210713312-ff62edc6-558d-496f-9375-9ba1ebdd1c73.png)

    
    
* 利用 split 切割檔案目錄   

      directory, name = os.path.split(filename)
      
    目錄路徑: directory =>
      
    ![image](https://user-images.githubusercontent.com/112489587/210713522-437953d7-dd9a-4d36-bf36-506f86d94c21.png)
    
    檔名: name => 
    ![image](https://user-images.githubusercontent.com/112489587/210713578-f801254d-0bfe-4fb5-a6fe-588f35f7396f.png)

    
* 利用 join 組合檔案目錄名稱      

       Path = os.path.join(directory, name)
    
    組合路徑: Path =>   
    ![image](https://user-images.githubusercontent.com/112489587/210713717-351895f4-fc1c-46a9-8d9a-38733f327a0f.png)


        # join函式,可以將參數內的字串結合成一個檔案的路徑,參數可以2個或2個以上
        # Drive,fpath=os.path.splitdirve(filename)
        # print('磁碟機:'+Drive)
        # print('路徑名稱:'+fpath)
#### 檔案大小
         
        os.path.getsize(filename)
        
![image](https://user-images.githubusercontent.com/112489587/210713961-b32981ea-157f-48f2-a27e-f2492755a6ab.png)

    
#### 判別檔案是否為目錄 回傳 bool
    
    isdir = os.path.isdir(filename)
    
![image](https://user-images.githubusercontent.com/112489587/210714080-5ab80c51-0e90-480f-ae22-899d4b1e8bff.png)
    

#### remove 刪除指定的檔案,配合語法 os.path.exists

    file = '/home/runner/ospathMo-ZumyFile.txt'
    if os.path.exists(file):
      os.remove(file)
    else:
      print(file + '檔案未建立!')

#### mkdir 建立指定的目錄

    dir = '/home/runner/ospathMo-Zu'  
    * 檢查目錄是否存在
    if not os.path.exists(dir):
      os.mkdir(dir)
    else:
      print(dir + '已經建立!')


#### rmdir 刪除指定的檔案,必須先刪除該目錄的檔案

    dir = '/home/runner/ospathMo-Zu' 
    * 檢查目錄是否存在
    if not os.path.exists(dir):
      os.rmkdir(dir)  
    else:
      print(dir + '目錄未建立!')





https://www.runoob.com/python/python-os-path.html
