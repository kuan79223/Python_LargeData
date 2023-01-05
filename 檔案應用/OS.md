    import os
#### getcwd 取得目前的工作目錄
    os.getcwd()

#### python 檔案路徑
    print(os.getcwd())
* 絕對路徑
    dir = '/home/runner/ospathbasename/content.txt'

#### 取出路徑中的檔案名稱
    print(os.path.basename(dir))

out >> content.txt

### '''將副檔名去除,留下檔案名稱'''

    basename1 = os.path.basename(dir).split('.')[0]
    print(basename1)

    basename2 = os.path.splitext(os.path.basename(dir))[0]
    print(basename2)

out >> content


#### remove 刪除指定的檔案,配合語法 os.path.exists

    file = 'myFile.txt'
    if os.path.exists(file):
      os.remove(file)
    else:
      print(file + '檔案未建立!')

#### mkdir 建立指定的目錄

    dir = 'myDir'  
    * 檢查目錄是否存在
    if not os.path.exists(dir):
      os.mkdir(dir)
    else:
      print(dir + '已經建立!')


#### rmdir 刪除指定的檔案,必須先刪除該目錄的檔案

    dir = 'myDir' 
    * 檢查目錄是否存在
    if not os.path.exists(dir):
      os.rmkdir(dir)  
    else:
      print(dir + '目錄未建立!')





https://www.runoob.com/python/python-os-path.html
