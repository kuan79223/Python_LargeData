#### 返回指定路徑下的文件和文件夾列表。
os.listdir(os.path.join(最外層資料夾 , 資料夾, 檔案名稱)



* os.walk() 方法用於通過在目錄樹中游走輸出在目錄中的文件名，向上或向下。

* os.walk()方法是一個簡單易用的文件、目錄遍歷器，可以幫助我們高效的處理文件、目錄方面的事情。


      import os
      for root, dirs, files in os.walk(".", topdown=False):
          for name in files:
              print(os.path.join(root, name))
          for name in dirs:
              print(os.path.join(root, name))

#### 操作系統_ walk ( top [, topdown = True [, onerror = None [, followlinks = False ]]])

* top  是你所要遍歷的目錄的地址，返回的是一個三元組(root,dirs,files)。
* root 所指的是當以前在遍歷的這個文件夾的本體的地址
* dirs 是一個列表，內容是該文件夾中所有的目錄的名稱(不包子目錄)
* files 同樣是 list , 內容是該文件夾中所有的文件(不包子目錄)
* topdown 可選，為True，則優先遍歷top目錄，否則優先遍歷top的子目錄(默認為開啟)。如果topdown參數為True，則walk遍歷top文件夾，與top文件夾子中每個子。

* onerror 可選，需要一個callable對象，當walk需要異常時，會調用。

* followlinks 可選，如果為True，則會遍歷目錄下的快捷方式(linux下是軟連接符號鏈接)實際所指的目錄(默認關閉)，如果為False，則優先遍歷top的子目錄。


      list1 = ['a', 'c', 'b']
      list2 = ['a', 'b']

      匹配檔案路徑是否一樣 
      match_list = set(list1) & set(list2)

out >> ['a', 'b']







參考文獻:
cmd快速抓取                       https://limitironbox.myds.me/wordpress/%E5%88%A9%E7%94%A8cmd%E5%BF%AB%E9%80%9F%E5%88%97%E5%87%BA%E8%B3%87%E6%96%99%E5%A4%BE%E5%85%A7%E7%9A%84%E6%AA%94%E6%A1%88%E5%90%8D%E7%A8%B1/                   
python 好用套件：利用 glob 抓取路徑下檔案名稱                   
https://ithelp.ithome.com.tw/articles/10262521
